package p4bd.ca1.reducers;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class LetterAvgReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {

    @Override
    protected void reduce(Text key, Iterable<DoubleWritable> values, Context context)
            throws IOException, InterruptedException {

        // The project relies on 1 file per language, thus the
        int sum = 0;
        for (DoubleWritable val : values)
            sum += val.get();

        // As per assignment spec: "...use HDFS and MapReduce to calculate average letter frequencies
        // across a number of languages".
        // Therefore, letter average = letter units (sum) / n. of languages (input files).
        // Important: Some languages (e.g. German) have exclusive letters, which makes this
        // average approach not accurate.
        int languages = context.getConfiguration().getInt("amount.languages", 1);
        context.write(key, new DoubleWritable((double)sum/languages));
    }
}
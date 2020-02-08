import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class AvgReducer extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {

    public void reduce(Text key, Iterable<DoubleWritable> values, Context context)
            throws IOException, InterruptedException {

        System.out.println(String.format("Kicking-of AvgReducer for [values=%s, context=%s]", values, context));
        System.err.println(String.format("Kicking-of AvgReducer for [values=%s, context=%s]", values, context));

        double wordQntChars = 0;
        int valuesSize = 0;
        System.out.println(" In Reducer now!");
        for (DoubleWritable value : values) {
            wordQntChars += value.get();
            valuesSize++;
        }

        System.out.println(String.format("Amount of words starting with '%s' is '%s'", key, valuesSize));

        double wordLegnthAvg = valuesSize == 0 ? 0 : wordQntChars / valuesSize;
        System.out.println(String.format("Average length of words starting with '%s' is '%s", key, wordLegnthAvg));


        context.write(key, new DoubleWritable(wordLegnthAvg));
        System.out.println(String.format("AvgReducer done! [wordLegnthAvg=%s]", wordLegnthAvg));
    }
}


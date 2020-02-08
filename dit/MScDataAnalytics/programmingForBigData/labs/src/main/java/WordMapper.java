import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class WordMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        System.out.println(String.format("Kicking-of WordMapper for [key=%s, value=%s, context=%s]", key, value, context));
        System.err.println(String.format("Kicking-of WordMapper for [key=%s, value=%s, context=%s]", key, value, context));


        String s = value.toString();

        for (String word : s.split("\\W+")) {
            if (word.length() > 0) {
                context.write(new Text(word), new IntWritable(1));
            }
        }

        System.out.println("WordMapper done!");
    }
}


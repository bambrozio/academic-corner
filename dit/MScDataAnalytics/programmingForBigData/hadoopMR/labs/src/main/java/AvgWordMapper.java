import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

public class AvgWordMapper extends Mapper<LongWritable, Text, Text, DoubleWritable> {
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {

        System.out.println(String.format("Kicking-of AvgWordMapper for [key=%s, value=%s, context=%s]", key, value, context));
        System.err.println(String.format("Kicking-of AvgWordMapper for [key=%s, value=%s, context=%s]", key, value, context));


        String s = value.toString();

        for (String word : s.split("\\W+")) {
            if (word.length() > 0) {
                context.write(
                        new Text(String.valueOf(word.charAt(0))),
                        new DoubleWritable(word.length()));
            }
        }

        System.out.println("AvgWordMapper done!");
    }
}


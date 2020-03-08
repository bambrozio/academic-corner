import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class WordCalc {
    public static void main(String[] args) throws Exception {

        if (args.length != 3 || (!args[0].equals("sum") && !args[0].equals("avg"))) {
            System.err.println("Usage: WordCalc <sum|avg> <input path> <output path>");
            System.exit(-1); }

        System.out.println(" In Driver now!");

        Job job = Job.getInstance();
        job.setJarByClass(WordCalc.class);
        boolean isSum = args[0].equals("sum");

        String jobName = isSum ? "WordCount" : "WordAvg";
        job.setJobName(jobName);

        Class reducer = isSum ? SumReducer.class : AvgReducer.class;
        job.setReducerClass(reducer);

        Class mapper = isSum ? WordMapper.class : AvgWordMapper.class;
        job.setMapperClass(mapper);

        Class outPutValue = isSum ? IntWritable.class : DoubleWritable.class;
        job.setOutputValueClass(outPutValue);

        job.setOutputKeyClass(Text.class);
        FileInputFormat.addInputPath(job, new Path(args[1]));
        FileOutputFormat.setOutputPath(job, new Path(args[2]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}


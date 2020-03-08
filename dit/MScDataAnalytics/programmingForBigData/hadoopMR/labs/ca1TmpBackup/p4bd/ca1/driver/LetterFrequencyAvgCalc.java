package p4bd.ca1.driver;

import org.apache.commons.io.IOUtils;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileStatus;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Counter;
import org.apache.hadoop.mapreduce.Counters;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import p4bd.ca1.reducers.LetterAvgReducer;
import p4bd.ca1.mappers.LetterMapper;


public class LetterFrequencyAvgCalc {

    public static void main(String[] args) throws Exception {

        Configuration conf = new Configuration();

        // Thus, JVM params such as the implemented "-Dcase.sensitive=true" can be taken by the Job.
        // See the use of it in the LetterMapper.java
        GenericOptionsParser optionParser = new GenericOptionsParser(conf, args);
        String[] remainingArgs = optionParser.getRemainingArgs();

        if (remainingArgs.length != 2) {
            System.err.println("Usage: hadoop jar <jar file> [-Dcase.sensitive=true] <input hdfs path> <output hdfs path> \n" +
                    "e.g.: hadoop jar /root/bucket/ca1/LetterFrequencyAvgCalc.jar /user/root/ca1/ /user/root/ca1/sink/");
            System.exit(-1);
        }

        // Get a MR Job instance and set this application to the classpath.
        Job job = Job.getInstance(conf, "Letter Frequency Average Calculator");

//        The filename that the map is reading from
//        job.getConfiguration().get("mapreduce.map.input.file")

        job.setJarByClass(LetterFrequencyAvgCalc.class);

        // Point out the Mapper class
        job.setMapperClass(LetterMapper.class);

        // Point out the Reducer class also as a Combiner.
        // Although the combiner is optional, it reduces the amount of data transferred from the Mapper to the Reducer,
        // therefore improving throughput because combiners perform local aggregation of the intermediate outputs.
        job.setCombinerClass(LetterAvgReducer.class);

        // Point out the Reducer class
        job.setReducerClass(LetterAvgReducer.class);

        //TODO:
//        - Applications can use the Counter to report its statistics.
//        Applications can define arbitrary Counters (of type Enum) and update them via
//        Counters.incrCounter(Enum, long) or Counters.incrCounter(String, String, long)
//        in the map and/or reduce methods. These counters are then globally aggregated by the framework.
//        - All intermediate values associated with a given output key are subsequently
//        grouped by the framework, and passed to the Reducer(s) to determine the final
//        output. Users can control the grouping by specifying a Comparator via
//        Job.setGroupingComparatorClass(Class).
//        - The total number of partitions is the same as the number of reduce tasks for
//        the job. Users can control which keys (and hence records) go to which Reducer by
//        implementing a custom Partitioner.
//        - The right number of reduces seems to be 0.95 or 1.75 multiplied by
//        (<no. of nodes> * <no. of maximum containers per node>).
//        With 0.95 all of the reduces can launch immediately and start transferring map
//        outputs as the maps finish. With 1.75 the faster nodes will finish their first
//        round of reduces and launch a second wave of reduces doing a much better job of
//        load balancing.
//        - Partitioner controls the partitioning of the keys of the intermediate map-outputs
//        The total number of partitions is the same as the number of reduce tasks for the job.



        // Set the types for the key/value output files.
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(DoubleWritable.class);

        // Each file has a different language. The number of files is the number of languages to be
        // used in the average letter calculation.
        FileSystem fs = FileSystem.get(conf);
        FileStatus[] status = fs.listStatus(new Path(remainingArgs[0]));
        job.getConfiguration().setInt("amount.languages", status.length);
        for (int i = 0; i < status.length; i++) {
            FSDataInputStream inputStream = fs.open(status[i].getPath());
            String content = IOUtils.toString(inputStream, "UTF-8");
        }

        // Load the input hdfs dataset path from the user input arguments.
        FileInputFormat.addInputPath(job, new Path(remainingArgs[0]));

        // Load the output hdfs folder path  from the user input arguments.
        FileOutputFormat.setOutputPath(job, new Path(remainingArgs[1]));

        // Exit the application when the job is complete.
        int exitCode = job.waitForCompletion(true) ? 0 : 1;

        System.out.println("Job concluded!");

        Counters counters = job.getCounters();
        Counter discardedChars = counters.findCounter(LetterMapper.LetterMapperCounters.DISCARDED_CHARS);
        System.out.println("Mapper Counter track - Frequency of ignored characters: " + discardedChars.getValue());

        System.exit(exitCode);
    }
}

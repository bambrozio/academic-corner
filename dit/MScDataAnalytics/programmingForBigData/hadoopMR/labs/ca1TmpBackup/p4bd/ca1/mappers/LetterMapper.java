package p4bd.ca1.mappers;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;
import java.util.StringTokenizer;

public class LetterMapper extends Mapper<Object, Text, Text, DoubleWritable> {

    public static enum LetterMapperCounters{ DISCARDED_CHARS }

    private final static DoubleWritable ONE = new DoubleWritable(1);
    private Text letter = new Text();
    private boolean caseSensitive;
    private Configuration conf;

    @Override
    protected void setup(Context context) throws IOException, InterruptedException {
        super.setup(context);
        conf = context.getConfiguration();

        // With that, user can set case sensitive through JVM parameter. e.g:
        // -Dcase.sensitive=true
        caseSensitive = conf.getBoolean("case.sensitive", false);
    }

    @Override
    protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        StringTokenizer itr = new StringTokenizer(value.toString());
        while (itr.hasMoreTokens()) {

            String rawLine = itr.nextToken();

            // Using counters to track how many non-alphabetic characters have been discarded
            int discardedChars = rawLine.replaceAll("[a-zA-ZÄÖÜäöüß]", "").length();
            context.getCounter(LetterMapperCounters.DISCARDED_CHARS).increment(discardedChars);

            // Regex to remove characters that are not either in the English, Italian or German alphabets.
            // Note: Output file will demand ISO-8859-1 reader encoding.
            String line = rawLine.replaceAll("[^a-zA-ZÄÖÜäöüß]", "");

            // case sensitive if user has set it.
            line = (caseSensitive) ? line : line.toLowerCase();

            // Iterate over each letter to map them unitarily.
            for (int i = 0; i < line.length(); i++) {
                letter.set(new byte[]{(byte) line.charAt(i)});
                context.write(letter, ONE);
            }
        }
    }
}

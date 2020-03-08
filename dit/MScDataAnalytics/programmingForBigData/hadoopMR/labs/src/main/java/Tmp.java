import org.apache.commons.io.filefilter.WildcardFileFilter;

import java.io.FileFilter;
import java.util.Locale;

public class Tmp {
    public static void main(String[] args) {
//        String word = "teStweiß nicht, cabeça ć č ob der Schlüssel zu A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, Ä, Ö, Ü, ß Statt dessen";
//        System.out.println(word.replaceAll("[^a-zA-ZÄÖÜäöüß]", ""));

//        System.out.println("++++++++++++testsssss");
        //TODO: Remove-me from here.
//        The filename that the map is reading from
//        job.getConfiguration().get("mapreduce.map.input.file")

//        FileFilter ff = new WildcardFileFilter("*.txt");
//        String path = "hdfs://hadoop-hadoop-hdfs-nn:9000/user/root/ca1/English.txt";
//        String[] pathElements = path.split("/");
//        String fileName = pathElements[pathElements.length-1];
//        System.out.println(fileName);
//        System.out.println(pattern);
//        System.out.println(fileName.matches(ff));

//        System.out.println(Locale.ITALIAN);


//        int letterFreq = 5;
//        int languages = 3;
//        double letterAvg = (double)letterFreq / languages;
//        System.out.println(letterAvg);

//        for (int i=0; i< 100; i++) {
//            double randomDouble = Math.random();
//            randomDouble = randomDouble * 3;
//            int randomInt = (int) randomDouble;
//            System.out.println(randomInt);
//        }

//        for (int i=0; i< 100; i++) {
//            int numPartitions = 2;
//            if (numPartitions < 1) {
//                System.out.println("here ---> " + 0);
//            }
//            double random = Math.random();
//            random = random * numPartitions;
//            int randomInt = (int) random;
//            System.out.println(randomInt);
//        }

        String line = "Italian.txt\ta\t21406";
        System.out.println(line.split("\t")[1]);
        System.out.println(line.split("\t")[2]);
    }
}

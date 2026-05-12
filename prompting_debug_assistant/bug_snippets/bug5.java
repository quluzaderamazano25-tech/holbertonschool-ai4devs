import java.util.HashMap;
import java.util.Map;

public class WordCounter {

    public static Map<String, Integer> countWords(String sentence) {
        Map<String, Integer> counts = new HashMap<>();
        String[] words = sentence.toLowerCase().split(" ");

        for (String word : words) {
            counts.put(word, counts.get(word) + 1);
        }
        return counts;
    }

    public static String mostFrequent(Map<String, Integer> counts) {
        String best = null;
        int max = 0;
        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            if (entry.getValue() >= max) {
                max = entry.getValue();
                best = entry.getKey();
            }
        }
        return best;
    }

    public static void main(String[] args) {
        String sentence = "the cat sat on the mat the cat";
        Map<String, Integer> result = countWords(sentence);
        System.out.println("Most frequent: " + mostFrequent(result));

        countWords(null);
    }
}
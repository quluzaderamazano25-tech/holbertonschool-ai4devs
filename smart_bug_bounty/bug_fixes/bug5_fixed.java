import java.util.HashMap;
import java.util.Map;

public class WordCounter {
    public static Map<String, Integer> countWords(String sentence) {
        // Null və boş cümlə yoxlanışı əlavə edildi
        if (sentence == null || sentence.isEmpty()) {
            return new HashMap<>();
        }
        
        Map<String, Integer> counts = new HashMap<>();
        String[] words = sentence.toLowerCase().split(" ");
        
        for (String word : words) {
            int currentCount = counts.getOrDefault(word, 0);
            counts.put(word, currentCount + 1);
        }
        return counts;
    }
}
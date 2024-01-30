//solution 1
//time complexity: O(n * k), where n is the number of strings and k is the longest length of the strings.
//space complexity:O(c) space, where c is the number of characters common to all strings.
import java.util.*;

class Program {
  public String[] commonCharacters(String[] strings) {
    HashMap<Character, Integer> characterCount = new HashMap<>();
    for (String string : strings) {
      HashSet<Character> unique = new HashSet<>();
      for (int i = 0; i < string.length(); i++) {
        unique.add(string.charAt(i));
      }
      for (char character : unique) {
        if (!characterCount.containsKey(character)) {
          characterCount.put(character, 0);
        }
        characterCount.put(character, characterCount.get(character) + 1);
      }
    }
    ArrayList<String> finalCharacters = new ArrayList<>();
    for (Map.Entry<Character, Integer> entry : characterCount.entrySet()) {
      if (entry.getValue() == strings.length) {
        finalCharacters.add(entry.getKey().toString());
      }
    }
    return finalCharacters.toArray(new String[0]);
  }
}

//solution2 
//same complexity as solution 1
import java.util.*;

class Program {
  public String[] commonCharacters(String[] strings) {
    HashMap<Character, Integer> characterCount = new HashMap<>();
    for (String string : strings) {
      HashSet<Character> unique = new HashSet<>();
      for (int i = 0; i < string.length(); i++) {
        unique.add(string.charAt(i));
      }
      for (char character : unique) {
        characterCount.put(character, characterCount.getOrDefault(character, 0) + 1);
      }
    }

    // First, count how many characters are common to all strings
    int commonCount = 0;
    for (int count : characterCount.values()) {
      if (count == strings.length) {
        commonCount++;
      }
    }
    
    // Create an array of the right size
    String[] finalCharacters = new String[commonCount];
    int index = 0;
    
    // Fill the array with the common characters
    for (Map.Entry<Character, Integer> entry : characterCount.entrySet()) {
      if (entry.getValue() == strings.length) {
        finalCharacters[index++] = entry.getKey().toString();
      }
    }
    
    return finalCharacters;
  }
}

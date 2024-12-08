import java.util.*;

public class helpers {
  public static List<List<Integer>> parseInput(String puzzleInput) {
    List<Integer> left = new ArrayList<>();
    List<Integer> right = new ArrayList<>();

    String[] lines = puzzleInput.trim().split("\n");
    for (String line : lines) {
      String[] parts = line.split("   ");
      left.add(Integer.parseInt(parts[0]));
      right.add(Integer.parseInt(parts[1]));
    }

    Collections.sort(left);
    Collections.sort(right);

    List<List<Integer>> result = new ArrayList<>();
    result.add(left);
    result.add(right);
    return result;
  }
}

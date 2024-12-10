import java.util.*;

public class helpers {
  public static List<List<Integer>> parseInput(final String puzzleInput) {
    final List<Integer> left = new ArrayList<>();
    final List<Integer> right = new ArrayList<>();

    final String[] lines = puzzleInput.trim().split("\n");
    for (final String line : lines) {
      final String[] parts = line.split("   ");
      left.add(Integer.parseInt(parts[0]));
      right.add(Integer.parseInt(parts[1]));
    }

    Collections.sort(left);
    Collections.sort(right);

    final List<List<Integer>> result = new ArrayList<>();
    result.add(left);
    result.add(right);
    return result;
  }
}

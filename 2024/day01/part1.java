import java.util.List;

public class part1 {
  public static Object solve(final String puzzleInput) {
    final List<List<Integer>> parsedInput = helpers.parseInput(puzzleInput);
    final List<Integer> left = parsedInput.get(0);
    final List<Integer> right = parsedInput.get(1);

    int sum = 0;
    for (int i = 0; i < left.size(); i++) {
      sum += Math.abs(left.get(i) - right.get(i));
    }
    return sum;
  }
}

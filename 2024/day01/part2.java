import java.util.*;
import java.util.stream.Collectors;

public class part2 {
  public static Object solve(final String puzzleInput) {
    final List<List<Integer>> parsedInput = helpers.parseInput(puzzleInput);
    final List<Integer> left = parsedInput.get(0);
    final List<Integer> right = parsedInput.get(1);

    final Map<Integer, Long> count =
        left.stream().collect(Collectors.groupingBy(i -> i, Collectors.counting()));

    return right.stream()
        .filter(count::containsKey)
        .mapToLong(item -> item * count.get(item))
        .sum();
  }
}

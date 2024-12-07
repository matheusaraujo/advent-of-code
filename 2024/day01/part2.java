import java.util.*;
import java.util.stream.Collectors;

public class part2 {
    public static Object solve(String puzzleInput) {
        List<List<Integer>> parsedInput = helpers.parseInput(puzzleInput);
        List<Integer> left = parsedInput.get(0);
        List<Integer> right = parsedInput.get(1);

        Map<Integer, Long> count = left.stream()
                                       .collect(Collectors.groupingBy(i -> i, Collectors.counting()));


        long result = right.stream()
                           .filter(count::containsKey)
                           .mapToLong(item -> item * count.get(item))
                           .sum();

        return result;
    }
}

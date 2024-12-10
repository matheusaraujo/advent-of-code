public class part1 {
  public static Object solve(final String puzzleInput) {
    return count(puzzleInput, '(') - count(puzzleInput, ')');
  }

  public static int count(final String input, final char target) {
    int count = 0;
    for (int i = 0; i < input.length(); i++) {
      if (input.charAt(i) == target) {
        count++;
      }
    }
    return count;
  }
}

public class part2 {
  private static final char OPEN = '(';

  public static Object solve(final String puzzleInput) {
    int floor = 0;
    int i = 0;

    for (; i < puzzleInput.length(); i++) {
      if (puzzleInput.charAt(i) == OPEN) {
        floor++;
      } else {
        floor--;
      }

      if (floor == -1) {
        break;
      }
    }
    return floor == -1 ? i + 1 : 0;
  }
}

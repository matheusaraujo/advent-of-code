public class Part1 {
    public static Object solve(String puzzleInput) {
        return count(puzzleInput, '(') - count(puzzleInput, ')');
    }

    private static int count(String input, char target) {
        int count = 0;

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == target) {
                count++;
            }
        }

        return count;
    }
}

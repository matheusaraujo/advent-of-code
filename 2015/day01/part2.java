public class part2 {
        public static Object solve(String puzzleInput) {
        int floor = 0;

        for (int i = 0; i < puzzleInput.length(); i++) {
            if (puzzleInput.charAt(i) == '(') {
                floor++;
            } else {
                floor--;
            }

            if (floor == -1) {
                return i + 1;
            }
        }

        return 0;
    }
}
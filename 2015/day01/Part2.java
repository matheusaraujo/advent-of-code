public class Part2 {
    public static Object solve(String puzzleInput) {
        int floor = 0;

        for (int i = 0; i < puzzleInput.length(); i++) {
            floor += puzzleInput.charAt(i) == '(' ? 1 : -1;
            if (floor == -1)
                return i + 1;
        }

        return 0;
    }
}

namespace aoc;

public static class Part2
{
    public static object Solve(string puzzleInput)
    {
        int floor = 0;

        for (int i = 0; i < puzzleInput.Length; i++)
        {
            floor += puzzleInput[i] == '(' ? 1 : -1;
            if (floor == -1)
                return i + 1;
        }

        return 0;
    }
}

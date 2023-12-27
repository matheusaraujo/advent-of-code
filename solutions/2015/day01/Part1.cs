namespace aoc;

public static class Part1
{
    public static object Solve(string puzzleInput)
    {
        return puzzleInput.Count('(') - puzzleInput.Count(')');
    }

    static int Count(this string input, char target)
    {
        var count = 0;
        foreach (char ch in input)
            if (ch == target)
                count++;
        return count;
    }
}
namespace aoc;

public static class Part1
{
    public static object Solve(string puzzleInput)
    {
        var (left, right) = Helpers.ParseInput(puzzleInput);
        return left.Zip(right, (l, r) => Math.Abs(l - r)).Sum();
    }
}

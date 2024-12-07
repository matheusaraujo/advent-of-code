namespace aoc;

public static class Part2
{
    public static object Solve(string puzzleInput)
    {
        var (left, right) = Helpers.ParseInput(puzzleInput);

        var count = left.GroupBy(x => x).ToDictionary(group => group.Key, group => group.Count());

        var result = right.Where(count.ContainsKey).Sum(item => item * count[item]);

        return result;
    }
}

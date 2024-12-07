namespace aoc;

public static class Helpers
{
    public static (List<int>, List<int>) ParseInput(string puzzleInput)
    {
        List<int> left = new(),
            right = new();

        foreach (var line in puzzleInput.Trim().Split('\n'))
        {
            var parts = line.Split("   ");
            left.Add(int.Parse(parts[0]));
            right.Add(int.Parse(parts[1]));
        }

        left.Sort();
        right.Sort();

        return (left, right);
    }
}

namespace aoc;

public class PuzzlePart
{
    public required Boolean Solved { get; set; }
    public required String OutputFile { get; set; }
}

public class Puzzle
{
    public required string Title { get; set; }
    public required string Year { get; set; }
    public required string Day { get; set; }
    public required string InputFile { get; set; }

    public required PuzzlePart Part1 { get; set; }
    public required PuzzlePart Part2 { get; set; }
}
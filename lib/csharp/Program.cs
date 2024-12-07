namespace aoc;

public class Program
{
    static void Main(string[] args)
    {
        string part = args[2];
        string input, puzzleInput = "";

        while ((input = Console.ReadLine()) != null)
            puzzleInput += input + "\n";

        if (part == "part1")
            Console.WriteLine(Part1.Solve(puzzleInput));
        else if (part == "part2")
            Console.WriteLine(Part2.Solve(puzzleInput));
    }
}
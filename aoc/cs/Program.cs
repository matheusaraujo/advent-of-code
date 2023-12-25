using System.Text;
using System.Text.Json;
using Xunit;
using Spectre.Console;

namespace aoc;

public class PuzzlePart
{
    public required Boolean Solved { get; set; }
    public required String Output_file { get; set; }
}

public class Puzzle
{
    public required string Title { get; set; }
    public required string Year { get; set; }
    public required string Day { get; set; }
    public required string Input_file { get; set; }

    public required PuzzlePart Part1 { get; set; }
    public required PuzzlePart Part2 { get; set; }
}

public class Program
{
    static readonly JsonSerializerOptions serializerOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase
    };

    static void Main()
    {
        var filePath = "data/2015-01.json";

        var jsonString = File.ReadAllText(filePath);
        var data = JsonSerializer.Deserialize<Puzzle>(jsonString, serializerOptions);

        if (data == null)
        {
            Console.WriteLine("File not found!");
            return;
        }

        Console.WriteLine(
            $"csharp: Running AOC {data.Year} Day {data.Day} - {data.Title}"
        );

        var input = File.ReadAllText(data.Input_file);

        var expectedAnswerPart1 = File.ReadAllText(data.Part1.Output_file);
        DateTime start1 = DateTime.Now;
        var answerPart1 = Part1.Solve(input);
        DateTime end1 = DateTime.Now;
        Assert.Equal(expectedAnswerPart1.ToString(), answerPart1.ToString());
        TimeSpan ts1 = end1 - start1;
        PrintAnswer("1", answerPart1, ts1);

        var expectedAnswerPart2 = File.ReadAllText(data.Part2.Output_file);
        DateTime start2 = DateTime.Now;
        var answerPart2 = Part2.Solve(input);
        DateTime end2 = DateTime.Now;
        Assert.Equal(expectedAnswerPart2.ToString(), answerPart2.ToString());
        TimeSpan ts2 = end2 - start2;
        PrintAnswer("2", answerPart2, ts2);

    }

    static void PrintAnswer(string part, object answer, TimeSpan executionTime)
    {
        AnsiConsole.Markup($"[purple]Part {part}:[/] " +
            $"[green]{answer}[/]" +
            $"[#808080 italic] (executed in {executionTime.TotalMilliseconds}ms)[/]" + "\n");
    }

}


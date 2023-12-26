using System.Text;
using System.Text.Json;
using Xunit;
using Spectre.Console;

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

public class Program
{
    static readonly JsonSerializerOptions serializerOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase
    };

    static void Main(string[] args)
    {
        var filePath = $"data/{args[0]}-{args[1]}.json";

        var jsonString = File.ReadAllText(filePath);
        var data = JsonSerializer.Deserialize<Puzzle>(jsonString, serializerOptions);

        if (data == null)
        {
            Console.WriteLine("File not found!");
            return;
        }

        Console.WriteLine(
            $"csharp: Running AoC {data.Year} Day {data.Day} - {data.Title}"
        );

        var input = File.ReadAllText(data.InputFile);

        var expectedAnswerPart1 = File.ReadAllText(data.Part1.OutputFile);
        DateTime start1 = DateTime.Now;
        var answerPart1 = Part1.Solve(input);
        DateTime end1 = DateTime.Now;
        Assert.Equal(expectedAnswerPart1.ToString(), answerPart1.ToString());
        TimeSpan ts1 = end1 - start1;
        PrintAnswer("1", answerPart1, ts1);

        var expectedAnswerPart2 = File.ReadAllText(data.Part2.OutputFile);
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
            $"[#909090 italic] (executed in {string.Format("{0:N2}", executionTime.TotalMilliseconds)}ms)[/]" + "\n");
    }

}


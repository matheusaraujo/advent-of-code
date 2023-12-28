using Spectre.Console;
using System.Text.Json;

namespace aoc;

public class Program
{
    static readonly JsonSerializerOptions serializerOptions = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase
    };

    static void Main(string[] args)
    {
        var jsonString = File.ReadAllText(args[0]);
        var puzzle = JsonSerializer.Deserialize<Puzzle>(jsonString, serializerOptions);

        if (puzzle == null)
        {
            Console.WriteLine("File not found!");
            Environment.Exit(1);
        }

        Console.WriteLine($"csharp: {puzzle.Title}");

        var input = File.ReadAllText(puzzle.InputFile);

        Run("Part 1", input, Part1.Solve, puzzle.Part1.OutputFile);
        Run("Part 1", input, Part2.Solve, puzzle.Part2.OutputFile);
    }

    public static void Run(string part, string input, Func<string, object> f, string outputFile = "")
    {
        var startTime = DateTime.Now;
        var receivedAnswer = f(input);
        var endTime = DateTime.Now;
        var executionTime = endTime - startTime;

        var checkedResult = "";
        string expectedAnswer;

        if (outputFile != "")
        {
            expectedAnswer = File.ReadAllText(outputFile);
            checkedResult = receivedAnswer.ToString() == expectedAnswer ? "[green]\u2714\uFE0E[/]" : "[red]\u2717\uFE0E[/]";
        }

        AnsiConsole.Markup($"[purple]{part}:[/] " +
            $"[green]{receivedAnswer}[/]" +
            $"[#909090 italic] (executed in {string.Format("{0:N2}", executionTime.TotalMilliseconds)}ms)[/] "
            + $" {checkedResult}\n"
        );

        if (checkedResult == "")
        {
            Console.WriteLine($"{part} Failed - Expected result: {receivedAnswer}");
            Environment.Exit(1);
        }
    }
}


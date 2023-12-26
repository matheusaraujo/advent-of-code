define run-csharp
	@mv aoc/csharp/Part1.cs aoc/csharp/_Part1.tmp
	@mv aoc/csharp/Part2.cs aoc/csharp/_Part2.tmp
	@cp ${year}/day${day}/Part1.cs aoc/csharp/Part1.cs
	@cp ${year}/day${day}/Part2.cs aoc/csharp/Part2.cs
	@dotnet run --project aoc/csharp/run.csproj ${year} ${day} || true
	@rm aoc/csharp/Part1.cs
	@rm aoc/csharp/Part2.cs
	@mv aoc/csharp/_Part1.tmp aoc/csharp/Part1.cs
	@mv aoc/csharp/_Part2.tmp aoc/csharp/Part2.cs
endef
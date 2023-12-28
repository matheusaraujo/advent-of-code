define run-csharp
	@ln -sf $(1)/Part1.cs ${CURDIR}/aoc/csharp/Part1.cs
	@ln -sf $(1)/Part2.cs ${CURDIR}/aoc/csharp/Part2.cs
	@dotnet run --project aoc/csharp/run.csproj $(2)
endef
define run-csharp
	@ln -sf ${CURDIR}/${year}/day${day}/Part1.cs ${CURDIR}/aoc/csharp/Part1.cs
	@ln -sf ${CURDIR}/${year}/day${day}/Part2.cs ${CURDIR}/aoc/csharp/Part2.cs
	@dotnet run --project aoc/csharp/run.csproj ${year} ${day} || true
endef
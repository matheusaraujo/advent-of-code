prepare:
	@cd aoc && pip install -r requirements.txt

load-puzzle: check_year_and_day
	@python3 aoc/py/load_puzzle.py $(year) $(day)

prepare-py:
	@pip install -r aoc/py/requirements.txt

prepare-cs:
	@dotnet restore aoc/csharp/run.csproj

run-py: check_year_and_day
	@python3 aoc/py/run.py $(year) $(day)

run-js: check_year_and_day
	@node aoc/js/run.js ${year} ${day}

run-csharp: check_year_and_day
	@mv aoc/csharp/Part1.cs aoc/csharp/_Part1.tmp
	@mv aoc/csharp/Part2.cs aoc/csharp/_Part2.tmp
	@cp ${year}/day${day}/Part1.cs aoc/csharp/Part1.cs
	@cp ${year}/day${day}/Part2.cs aoc/csharp/Part2.cs
	@dotnet run --project aoc/csharp/run.csproj ${year} ${day} || true
	@rm aoc/csharp/Part1.cs
	@rm aoc/csharp/Part2.cs
	@mv aoc/csharp/_Part1.tmp aoc/csharp/Part1.cs
	@mv aoc/csharp/_Part2.tmp aoc/csharp/Part2.cs

run-java: check_year_and_day
	@mv aoc/java/Part1.java aoc/java/_Part1.tmp
	@mv aoc/java/Part2.java aoc/java/_Part2.tmp
	@cp ${year}/day${day}/Part1.java aoc/java/Part1.java
	@cp ${year}/day${day}/Part2.java aoc/java/Part2.java
	@rm -f aoc/java/*.class
	@javac aoc/java/Run.java aoc/java/Part1.java aoc/java/Part2.java
	@java -cp aoc/java Run ${year} ${day} || true
	@rm aoc/java/Part1.java
	@rm aoc/java/Part2.java
	@mv aoc/java/_Part1.tmp aoc/java/Part1.java
	@mv aoc/java/_Part2.tmp aoc/java/Part2.java

run-go: check_year_and_day
	@mv aoc/go/part1.go aoc/go/_part1.tmp
	@mv aoc/go/part2.go aoc/go/_part2.tmp
	@cp ${year}/day${day}/part1.go aoc/go/part1.go
	@cp ${year}/day${day}/part2.go aoc/go/part2.go
	@go run aoc/go/part1.go aoc/go/part2.go aoc/go/run.go ${year} ${day} || true
	@rm aoc/go/part1.go
	@rm aoc/go/part2.go
	@mv aoc/go/_part1.tmp aoc/go/part1.go
	@mv aoc/go/_part2.tmp aoc/go/part2.go

run-c: check_year_and_day
	@mv aoc/c/part1.c aoc/c/_part1.tmp
	@mv aoc/c/part2.c aoc/c/_part2.tmp
	@cp ${year}/day${day}/part1.c aoc/c/part1.c
	@cp ${year}/day${day}/part2.c aoc/c/part2.c
	@gcc -o aoc/c/run aoc/c/part1.c aoc/c/part2.c aoc/c/run.c || true
	@./aoc/c/run ${year} ${day} || true
	@rm aoc/c/part1.c
	@rm aoc/c/part2.c
	@mv aoc/c/_part1.tmp aoc/c/part1.c
	@mv aoc/c/_part2.tmp aoc/c/part2.c

check_year_and_day:
ifndef year
	@echo "[year] must be defined"
	@exit 1
else ifndef day
	@echo "[day] must be defined"
	@exit 1
endif
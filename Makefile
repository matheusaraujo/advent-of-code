prepare:
	@cd aoc && pip install -r requirements.txt

load-puzzle: check_year_and_day
	@python3 aoc/py/load_puzzle.py $(year) $(day)

prepare-py:
	@pip install -r aoc/py/requirements.txt

prepare-cs:
	@dotnet restore aoc/cs/run.csproj

run-py: check_year_and_day
	@python3 aoc/py/run.py $(year) $(day)

run-js: check_year_and_day
	@node aoc/js/run.js ${year} ${day}

run-cs: check_year_and_day
	@mv aoc/cs/Part1.cs aoc/cs/_Part1.tmp
	@mv aoc/cs/Part2.cs aoc/cs/_Part2.tmp
	@cp ${year}/day${day}/Part1.cs aoc/cs/Part1.cs
	@cp ${year}/day${day}/Part2.cs aoc/cs/Part2.cs
	@dotnet run --project aoc/cs/run.csproj ${year} ${day}
	@rm aoc/cs/Part1.cs
	@rm aoc/cs/Part2.cs
	@mv aoc/cs/_Part1.tmp aoc/cs/Part1.cs
	@mv aoc/cs/_Part2.tmp aoc/cs/Part2.cs

run-java: check_year_and_day
	@mv aoc/java/Part1.java aoc/java/_Part1.tmp
	@mv aoc/java/Part2.java aoc/java/_Part2.tmp
	@cp ${year}/day${day}/Part1.java aoc/java/Part1.java
	@cp ${year}/day${day}/Part2.java aoc/java/Part2.java
	@rm -f aoc/java/*.class
	@javac aoc/java/Run.java aoc/java/Part1.java aoc/java/Part2.java
	@java -cp aoc/java Run
	@rm aoc/java/Part1.java
	@rm aoc/java/Part2.java
	@mv aoc/java/_Part1.tmp aoc/java/Part1.java
	@mv aoc/java/_Part2.tmp aoc/java/Part2.java

check_year_and_day:
ifndef year
	@echo "[year] must be defined"
	@exit 1
else ifndef day
	@echo "[day] must be defined"
	@exit 1
endif
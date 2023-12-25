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
	@mv aoc/cs/part1.cs aoc/cs/_part1.tmp
	@mv aoc/cs/part2.cs aoc/cs/_part2.tmp
	@cp ${year}/day${day}/part1.cs aoc/cs/part1.cs
	@cp ${year}/day${day}/part2.cs aoc/cs/part2.cs
	@dotnet run --project aoc/cs/run.csproj ${year} ${day}
	@rm aoc/cs/part1.cs
	@rm aoc/cs/part2.cs
	@mv aoc/cs/_part1.tmp aoc/cs/part1.cs
	@mv aoc/cs/_part2.tmp aoc/cs/part2.cs

check_year_and_day:
ifndef year
	@echo "[year] must be defined"
	@exit 1
else ifndef day
	@echo "[day] must be defined"
	@exit 1
endif
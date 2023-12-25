prepare:
	@cd aoc && pip install -r requirements.txt

load-puzzle: check_year_and_day
	@python3 aoc/load_puzzle.py $(year) $(day)

run-py: check_year_and_day
	@python3 aoc/run.py $(year) $(day)

check_year_and_day:
ifndef year
	@echo "[year] must be defined"
	@exit 1
else ifndef day
	@echo "[day] must be defined"
	@exit 1
endif
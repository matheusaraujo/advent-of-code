hello-world:
	@echo "hello-world!"

prepare:
	@cd aoc && pip install -r requirements.txt

load-puzzle:
ifndef year
	@echo "[year] must be defined"
else ifndef day
	@echo "[day] must be defined"
else
	@python3 aoc/load-puzzle.py $(year) $(day)
endif
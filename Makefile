hello-world:
	@echo "hello-world!"

prepare:
	@cd aoc && pip install -r requirements.txt

init:
	@cd aoc && python3 run.py
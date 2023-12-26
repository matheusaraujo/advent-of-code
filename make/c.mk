define run-c
	@gcc -o aoc/c/run ${year}/day${day}/part1.c ${year}/day${day}/part2.c aoc/c/run.c || true
	@./aoc/c/run ${year} ${day} || true
endef

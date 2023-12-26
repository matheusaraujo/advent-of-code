define run-c
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
endef

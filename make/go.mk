define run-go
	@mv aoc/go/part1.go aoc/go/_part1.tmp
	@mv aoc/go/part2.go aoc/go/_part2.tmp
	@cp ${year}/day${day}/part1.go aoc/go/part1.go
	@cp ${year}/day${day}/part2.go aoc/go/part2.go
	@go run aoc/go/part1.go aoc/go/part2.go aoc/go/run.go ${year} ${day} || true
	@rm aoc/go/part1.go
	@rm aoc/go/part2.go
	@mv aoc/go/_part1.tmp aoc/go/part1.go
	@mv aoc/go/_part2.tmp aoc/go/part2.go
endef
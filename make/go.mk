define run-go
	@ln -sf ${CURDIR}/${year}/day${day}/part1.go ${CURDIR}/aoc/go/part1.go
	@ln -sf ${CURDIR}/${year}/day${day}/part2.go ${CURDIR}/aoc/go/part2.go
	@go run aoc/go/part1.go aoc/go/part2.go aoc/go/run.go ${year} ${day}
endef
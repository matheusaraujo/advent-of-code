define run-cpp
	@mv aoc/cpp/part1.cpp aoc/cpp/_part1.tmp
	@mv aoc/cpp/part2.cpp aoc/cpp/_part2.tmp
	@cp ${year}/day${day}/part1.cpp aoc/cpp/part1.cpp
	@cp ${year}/day${day}/part2.cpp aoc/cpp/part2.cpp
	@g++ -std=c++11 -o aoc/cpp/run aoc/cpp/part1.cpp aoc/cpp/part2.cpp aoc/cpp/run.cpp || true
	@./aoc/cpp/run ${year} ${day} || true
	@rm aoc/cpp/part1.cpp
	@rm aoc/cpp/part2.cpp
	@mv aoc/cpp/_part1.tmp aoc/cpp/part1.cpp
	@mv aoc/cpp/_part2.tmp aoc/cpp/part2.cpp
endef

define run-java
	@mv aoc/java/Part1.java aoc/java/_Part1.tmp
	@mv aoc/java/Part2.java aoc/java/_Part2.tmp
	@cp ${year}/day${day}/Part1.java aoc/java/Part1.java
	@cp ${year}/day${day}/Part2.java aoc/java/Part2.java
	@javac aoc/java/Run.java aoc/java/Part1.java aoc/java/Part2.java
	@java -cp aoc/java Run ${year} ${day} || true
	@rm aoc/java/Part1.java
	@rm aoc/java/Part2.java
	@mv aoc/java/_Part1.tmp aoc/java/Part1.java
	@mv aoc/java/_Part2.tmp aoc/java/Part2.java
endef
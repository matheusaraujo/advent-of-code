define run-java
	@javac aoc/java/Run.java ${year}/day${day}/Part1.java ${year}/day${day}/Part2.java
	@java -cp "${year}/day${day}:aoc/java" Run ${year} ${day}
endef
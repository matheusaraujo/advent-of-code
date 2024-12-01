function part2(puzzle_input) {
  floor = 0
  for(i = 0; i < puzzle_input.length; i++) {
      floor += puzzle_input[i] == "(" ? 1 : -1
      if (floor == -1) return i + 1;
  }

  return 0
}

module.exports = part2;
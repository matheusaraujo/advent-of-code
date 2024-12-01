function part2(puzzle_input) {
  let floor = 0;
  for (let i = 0; i < puzzle_input.length; i += 1) {
    floor += puzzle_input[i] === "(" ? 1 : -1;
    if (floor === -1) return i + 1;
  }
  return 0;
}

module.exports = part2;

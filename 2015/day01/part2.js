function part2(puzzleInput) {
  let floor = 0;
  for (let i = 0; i < puzzleInput[0].length; i += 1) {
    floor += puzzleInput[0][i] === "(" ? 1 : -1;
    if (floor === -1) return i + 1;
  }
  return 0;
}

module.exports = part2;

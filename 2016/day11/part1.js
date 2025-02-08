const { parseInput, solve } = require("./helpers");

function part1(puzzleInput) {
  const { floors } = parseInput(puzzleInput);
  const state = [0, floors];
  return solve(state);
}

module.exports = part1;

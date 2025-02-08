const { parseInput, solve } = require("./helpers");

function part2(puzzleInput) {
  const { floors, materialCount } = parseInput(puzzleInput);
  let state = [0, floors];
  state[1][0][0].push(materialCount, materialCount + 1);
  state[1][0][1].push(materialCount, materialCount + 1);
  return solve(state);
}

module.exports = part2;

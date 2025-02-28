const { parseInput, findFirstValidTime } = require("./helpers.js");

function part2(puzzleInput) {
  const discs = parseInput(puzzleInput);
  discs.push([11, 0]);
  return findFirstValidTime(discs);
}

module.exports = part2;

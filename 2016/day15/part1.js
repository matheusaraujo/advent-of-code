const { parseInput, findFirstValidTime } = require("./helpers.js");

function part1(puzzleInput) {
  return findFirstValidTime(parseInput(puzzleInput));
}

module.exports = part1;

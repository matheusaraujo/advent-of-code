const findKeyIndex = require("./helpers");

function part1(puzzleInput) {
  return findKeyIndex(puzzleInput[0], 64);
}

module.exports = part1;

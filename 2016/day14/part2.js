const findKeyIndex = require("./helpers");

function part2(puzzleInput) {
  return findKeyIndex(puzzleInput[0], 64, 2017);
}

module.exports = part2;

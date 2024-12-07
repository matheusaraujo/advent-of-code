const { parseInput } = require("./helpers");

const part1 = (puzzleInput) => {
  const { left, right } = parseInput(puzzleInput);
  return left.reduce((sum, l, index) => sum + Math.abs(l - right[index]), 0);
};

module.exports = part1;

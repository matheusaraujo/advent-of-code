const { parseInput } = require("./helpers");

const part2 = (puzzleInput) => {
  const { left, right } = parseInput(puzzleInput);

  const count = left.reduce((acc, value) => {
    acc[value] = (acc[value] || 0) + 1;
    return acc;
  }, {});

  return right.reduce((sum, item) => {
    if (count[item]) {
      sum += item * count[item];
    }
    return sum;
  }, 0);
};

module.exports = part2;

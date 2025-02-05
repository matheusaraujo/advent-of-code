const { swapCard, decodeScreen } = require("./helpers");

function part2(puzzleInput) {
  return decodeScreen(swapCard(puzzleInput));
}

module.exports = part2;

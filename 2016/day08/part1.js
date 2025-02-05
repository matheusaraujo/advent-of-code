const { swapCard } = require("./helpers");

function part1(puzzleInput) {
  const screen = swapCard(puzzleInput);
  let totalPixels = 0;

  for (const row of screen) {
    totalPixels += row.filter((pixel) => pixel === "#").length;
  }

  return totalPixels;
}

module.exports = part1;

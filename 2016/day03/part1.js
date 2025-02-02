let { parseLine, isTriangle } = require("./helpers.js");

function part1(puzzleInput) {
  let validTriangles = 0;
  for (const line of puzzleInput) {
    if (isTriangle(parseLine(line))) {
      validTriangles++;
    }
  }
  return validTriangles;
}

module.exports = part1;

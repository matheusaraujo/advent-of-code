const { parseLine, isTriangle } = require("./helpers.js");

function part2(puzzleInput) {
  let validTriangles = 0;
  for (let i = 2; i < puzzleInput.length; i += 3) {
    const [t1, t2, t3] = [
      parseLine(puzzleInput[i - 2]),
      parseLine(puzzleInput[i - 1]),
      parseLine(puzzleInput[i]),
    ];

    for (let j = 0; j < 3; j++) {
      if (isTriangle([t1[j], t2[j], t3[j]])) {
        validTriangles++;
      }
    }
  }
  return validTriangles;
}

module.exports = part2;

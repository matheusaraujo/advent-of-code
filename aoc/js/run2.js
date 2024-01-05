const fs = require("fs");

const part = process.argv[2];
const solutionDir = process.argv[3];
const puzzleInput = process.argv[4];

const part1path = "../../" + solutionDir + "/part1.js";
const part2path = "../../" + solutionDir + "/part2.js";
const part1 = require(part1path);
const part2 = require(part2path);

const run = function (f) {
  const startTime = performance.now();
  const receivedAnswer = f(puzzleInput);
  const endTime = performance.now();
  console.log(
    JSON.stringify({
      receivedAnswer,
      executionTime: (endTime - startTime).toFixed(2),
    })
  );
};

const main = function () {
  if (part == "part1") run(part1);
  else if (part == "part2") run(part2);
};

main();

const fs = require("fs");

const solutionDir = process.argv[2];
const jsonFile = process.argv[3];

const part1path = "../../" + solutionDir + "/part1.js";
const part2path = "../../" + solutionDir + "/part2.js";
const part1 = require(part1path);
const part2 = require(part2path);

const formatTime = function (executionTime) {
  return executionTime.toFixed(2) + "ms";
};

const puzzle = JSON.parse(fs.readFileSync(jsonFile, "utf8"));

const run = function (part, input, f, outputFile) {
  const expectedAnswer = fs.readFileSync(outputFile, "utf8");
  const startTime = performance.now();
  const receivedAnswer = f(input);
  const endTime = performance.now();
  const executionTime = formatTime(endTime - startTime);

  console.log(
    `\x1b[35m${part}: \x1b[32m${receivedAnswer}\x1b[3;90m (executed in ${executionTime})\x1b[0m`
  );

  if (expectedAnswer != receivedAnswer) {
    console.log(
      `${part} Failed - Expected: ${expectedAnswer} != received: ${receivedAnswer}`
    );
    process.exit(1);
  }
};

const main = function () {
  console.log(`js: ${puzzle.fullTitle}`);
  const input = fs.readFileSync(puzzle.inputFile, "utf8");

  run("Part 1", input, part1, puzzle.part1.outputFile);
  run("Part 2", input, part2, puzzle.part2.outputFile);
};

main();

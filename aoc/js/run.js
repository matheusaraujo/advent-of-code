const fs = require("fs");

const solutionDir = process.argv[2];
const jsonFile = process.argv[3];

const part1path = "../../" + solutionDir + "/part1.js";
const part2path = "../../" + solutionDir + "/part2.js";
const part1 = require(part1path);
const part2 = require(part2path);

const colors = {
  RESET: "\x1b[0m",
  PURPLE: "\x1b[35m",
  GREEN: "\x1b[32m",
  GREY: "\x1b[3;90m",
};

const symbols = {
  CHECK: `${colors.GREEN}\u2714\uFE0E${colors.RESET}`,
  CROSS: `${colors.RED}\u2717\uFE0E${colors.RESET}`,
};

const formatTime = function (executionTime) {
  return executionTime.toFixed(2) + "ms";
};

const puzzle = JSON.parse(fs.readFileSync(jsonFile, "utf8"));

const run = function (part, input, f, outputFile) {
  const startTime = performance.now();
  const receivedAnswer = f(input);
  const endTime = performance.now();
  const executionTime = formatTime(endTime - startTime);

  let checked = "";

  if (outputFile != undefined) {
    const expectedAnswer = fs.readFileSync(outputFile, "utf8");
    checked = receivedAnswer == expectedAnswer ? symbols.CHECK : symbols.CROSS;
  }

  console.log(
    `${colors.PURPLE}${part}: ${colors.GREEN}${receivedAnswer}` +
      `${colors.GREY} (executed in ${executionTime})${colors.RESET}` +
      ` ${checked}`
  );

  if (checked === "") {
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

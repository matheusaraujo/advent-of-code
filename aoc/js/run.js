const fs = require("fs");

const solutionDir = process.argv[2];
const jsonFile = process.argv[3];
const mode = process.argv[4];

const part1path = "../../" + solutionDir + "/part1.js";
const part2path = "../../" + solutionDir + "/part2.js";
const part1 = require(part1path);
const part2 = require(part2path);

const colors = {
  RESET: "\x1b[0m",
  PURPLE: "\x1b[35m",
  GREEN: "\x1b[32m",
  GREY: "\x1b[3;90m",
  RED: "\x1b[3;91m",
};

const symbols = {
  CHECK: `${colors.GREEN}\u2714\uFE0E${colors.RESET}`,
  CROSS: `${colors.RED}\u2717\uFE0E${colors.RESET}`,
};

const main = function () {
  const puzzle = JSON.parse(fs.readFileSync(jsonFile, "utf8"));
  console.log(`js(${mode}): ${puzzle.fullTitle}`);

  const modesDict = { part1: runPart1, part2: runPart2, solved: runSolved };
  modesDict[mode](puzzle);
};

const runPart1 = (puzzle) => runPart(puzzle.part1, part1);

const runPart2 = (puzzle) => runPart(puzzle.part2, part2);

const runPart = function (part, f) {
  for (const example of part.examples) {
    run(example.example, example.inputFile, f, example.outputFile);
  }
};

const runSolved = function (puzzle) {
  run(puzzle.part1.part, puzzle.inputFile, part1, puzzle.part1.outputFile);
  run(puzzle.part2.part, puzzle.inputFile, part2, puzzle.part2.outputFile);
};

const formatTime = function (executionTime) {
  return executionTime.toFixed(2) + "ms";
};

const run = function (part, inputFile, f, outputFile = undefined) {
  const input = fs.readFileSync(inputFile, "utf-8");
  const startTime = performance.now();
  const receivedAnswer = f(input);
  const endTime = performance.now();
  const executionTime = formatTime(endTime - startTime);

  if (outputFile == undefined) {
    printResult(part, receivedAnswer, executionTime);
  }

  // let checked = "";
  // let expectedAnswer = "";

  // if (outputFile != undefined) {
  //   expectedAnswer = fs.readFileSync(outputFile, "utf-8");
  //   // checked = receivedAnswer == expectedAnswer ? symbols.CHECK : symbols.CROSS;

  //   if (receivedAnswer == expectedAnswer) {
  //     checked = symbols.CHECK;
  //   } else {
  //   }
  // }

  // console.log(
  //   `${colors.PURPLE}${part}: ${colors.GREEN}${receivedAnswer}` +
  //     `${colors.GREY} (executed in ${executionTime})${colors.RESET}` +
  //     ` ${checked}`
  // );

  // if (checked === "") {
  //   console.log(
  //     `${part} Failed - Expected: ${expectedAnswer} != received: ${receivedAnswer}`
  //   );
  //   process.exit(1);
  // }
};

const handleExpectedResult = function () {};

const printResult = function (
  part,
  receivedAnswer,
  executionTime,
  checked = undefined
) {
  console.log(
    `${colors.PURPLE}${part}: ${colors.GREEN}${receivedAnswer}` +
      `${colors.GREY} (executed in ${executionTime})${colors.RESET}` +
      ` ${checked}`
  );
};
main();

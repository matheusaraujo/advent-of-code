const Computer = require("./helpers");

function part1(puzzleInput) {
  return new Computer(puzzleInput).execute();
}

module.exports = part1;

const Computer = require("./helpers");

function part1(puzzleInput) {
  return new Computer(puzzleInput, { c: 1 }).execute();
}

module.exports = part1;

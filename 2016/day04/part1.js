const Room = require("./helpers.js");

function part1(puzzleInput) {
  let result = 0;
  for (const line of puzzleInput) {
    const room = new Room(line);
    if (room.isReal()) {
      result += room.sectorId;
    }
  }
  return result;
}

module.exports = part1;

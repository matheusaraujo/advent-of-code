function parseLine(line) {
  return line.match(/\d+/g).map(Number);
}

function isTriangle(sides) {
  sides.sort((a, b) => a - b);
  return sides[0] + sides[1] > sides[2];
}

module.exports = { parseLine, isTriangle };

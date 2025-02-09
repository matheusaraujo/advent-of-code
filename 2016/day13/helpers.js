const directions = [
  { dx: 1, dy: 0 },
  { dx: -1, dy: 0 },
  { dx: 0, dy: 1 },
  { dx: 0, dy: -1 },
];

function isOpenSpace(x, y, favoriteNumber) {
  const value = x * x + 3 * x + 2 * x * y + y + y * y + favoriteNumber;
  const binaryOnes = value
    .toString(2)
    .split("")
    .filter((c) => c === "1").length;
  return binaryOnes % 2 === 0;
}

module.exports = { directions, isOpenSpace };

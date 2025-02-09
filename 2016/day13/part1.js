const { directions, isOpenSpace } = require("./helpers");

function part1(puzzleInput) {
  return shortestPath(parseInt(puzzleInput[0]), 31, 39);
}

function shortestPath(favoriteNumber, targetX, targetY) {
  const queue = [{ x: 1, y: 1, steps: 0 }];
  const visited = new Set();
  visited.add(`1,1`);

  while (queue.length > 0) {
    const { x, y, steps } = queue.shift();

    if (x === targetX && y === targetY) return steps;

    for (const { dx, dy } of directions) {
      const newX = x + dx;
      const newY = y + dy;

      if (
        newX >= 0 &&
        newY >= 0 &&
        !visited.has(`${newX},${newY}`) &&
        isOpenSpace(newX, newY, favoriteNumber)
      ) {
        visited.add(`${newX},${newY}`);
        queue.push({ x: newX, y: newY, steps: steps + 1 });
      }
    }
  }

  return -1;
}

module.exports = part1;

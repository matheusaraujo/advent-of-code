const { directions, isOpenSpace } = require("./helpers");

function part2(puzzleInput) {
  return countReachableLocations(parseInt(puzzleInput[0]), 50);
}

function countReachableLocations(favoriteNumber, maxSteps) {
  const queue = [{ x: 1, y: 1, steps: 0 }];
  const visited = new Map();
  visited.set(`1,1`, 0);

  while (queue.length > 0) {
    const { x, y, steps } = queue.shift();

    if (steps >= maxSteps) continue;

    for (const { dx, dy } of directions) {
      const newX = x + dx;
      const newY = y + dy;

      if (
        newX >= 0 &&
        newY >= 0 &&
        !visited.has(`${newX},${newY}`) &&
        isOpenSpace(newX, newY, favoriteNumber)
      ) {
        visited.set(`${newX},${newY}`, steps + 1);
        queue.push({ x: newX, y: newY, steps: steps + 1 });
      }
    }
  }

  return visited.size;
}

module.exports = part2;

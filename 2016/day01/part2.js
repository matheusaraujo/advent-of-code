function part2(puzzleInput) {
  const sequence = puzzleInput[0].split(", ");
  const position = [0, 0];
  const directions = ["N", "E", "S", "W"];
  let directionIndex = 0;
  const visited = new Set();

  function posKey(pos) {
    return `${pos[0]},${pos[1]}`;
  }

  visited.add(posKey(position));

  for (let instruction of sequence) {
    const turn = instruction[0];
    const distance = parseInt(instruction.slice(1), 10);

    if (turn === "L") directionIndex = (directionIndex - 1 + 4) % 4;
    else if (turn === "R") directionIndex = (directionIndex + 1) % 4;

    for (let i = 0; i < distance; i++) {
      if (directions[directionIndex] === "N") position[1] += 1;
      else if (directions[directionIndex] === "E") position[0] += 1;
      else if (directions[directionIndex] === "S") position[1] -= 1;
      else if (directions[directionIndex] === "W") position[0] -= 1;

      const key = posKey(position);
      if (visited.has(key))
        return Math.abs(position[0]) + Math.abs(position[1]);

      visited.add(key);
    }
  }

  return Math.abs(position[0]) + Math.abs(position[1]);
}

module.exports = part2;

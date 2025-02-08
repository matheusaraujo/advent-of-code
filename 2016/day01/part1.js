function part1(puzzleInput) {
  const sequence = puzzleInput[0].split(", ");
  const position = [0, 0];
  const directions = ["N", "E", "S", "W"];
  let directionIndex = 0;

  for (const instruction of sequence) {
    const turn = instruction[0];
    const distance = parseInt(instruction.slice(1), 10);

    if (turn === "L") directionIndex = (directionIndex - 1 + 4) % 4;
    else if (turn === "R") directionIndex = (directionIndex + 1) % 4;

    if (directions[directionIndex] == "N") position[1] += distance;
    else if (directions[directionIndex] == "E") position[0] += distance;
    else if (directions[directionIndex] == "S") position[1] -= distance;
    else if (directions[directionIndex] == "W") position[0] -= distance;
  }

  return Math.abs(position[0]) + Math.abs(position[1]);
}

module.exports = part1;

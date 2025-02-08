function solve(position, moves) {
  for (let move of moves) {
    if (move === "U" && position > 3) position -= 3;
    else if (move === "D" && position < 7) position += 3;
    else if (move === "L" && ![1, 4, 7].includes(position)) position -= 1;
    else if (move === "R" && ![3, 6, 9].includes(position)) position += 1;
  }
  return position;
}

function part1(puzzleInput) {
  let position = 5;
  let result = "";

  for (let line of puzzleInput) {
    position = solve(position, line);
    result += position.toString();
  }

  return result;
}

module.exports = part1;

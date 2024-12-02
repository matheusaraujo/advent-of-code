function countOccurrences(str, char) {
  return str.split(char).length - 1;
}

function part1(puzzleInput) {
  return (
    countOccurrences(puzzleInput, "(") - countOccurrences(puzzleInput, ")")
  );
}

module.exports = part1;

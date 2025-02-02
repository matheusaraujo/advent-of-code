function countOccurrences(str, char) {
  return str.split(char).length - 1;
}

function part1(puzzleInput) {
  return (
    countOccurrences(puzzleInput[0], "(") -
    countOccurrences(puzzleInput[0], ")")
  );
}

module.exports = part1;

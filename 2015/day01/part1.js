function countOccurrences(str, char) {
  return str.split(char).length - 1;
}

function part1(data) {
  return countOccurrences(data, "(") - countOccurrences(data, ")");
}

module.exports = part1;
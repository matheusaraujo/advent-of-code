function part1(puzzleInput) {
  return puzzleInput.map(countChars).reduce((a, b) => a + b, 0);
}

function countChars(str) {
  let count = 0;
  for (let i = 0; i < str.length; i++) {
    if (str[i] !== "(") {
      count++;
    } else {
      const end = str.indexOf(")", i);
      const [length, repeat] = str
        .slice(i + 1, end)
        .split("x")
        .map(Number);
      count += length * repeat;
      i = end + length;
    }
  }
  return count;
}

module.exports = part1;

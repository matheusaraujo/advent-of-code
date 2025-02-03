function solve(puzzleInput, mostCommon) {
  const length = puzzleInput[0].length;
  const frequency = Array.from({ length }, () => {});

  for (let i = 0; i < puzzleInput.length; i++) {
    for (let j = 0; j < length; j++) {
      const letter = puzzleInput[i][j];
      frequency[j] = frequency[j] || {};
      frequency[j][letter] = (frequency[j][letter] || 0) + 1;
    }
  }

  let result = "";

  for (let i = 0; i < length; i++) {
    const sorted = Object.entries(frequency[i]).sort((a, b) => b[1] - a[1]);
    const [letter] = mostCommon ? sorted[0] : sorted[sorted.length - 1];
    result += letter;
  }

  return result;
}

module.exports = solve;

const parseInput = (puzzleInput) => {
  const left = [];
  const right = [];

  puzzleInput.forEach((line) => {
    const parts = line.split("   ");
    left.push(parseInt(parts[0]));
    right.push(parseInt(parts[1]));
  });

  left.sort((a, b) => a - b);
  right.sort((a, b) => a - b);

  return { left, right };
};

module.exports = { parseInput };

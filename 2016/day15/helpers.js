function parseInput(puzzeInput) {
  return puzzeInput.map((line) => {
    const match = line.match(
      /Disc #\d+ has (\d+) positions; .* position (\d+)\./,
    );
    return [parseInt(match[1]), parseInt(match[2])];
  });
}

function findFirstValidTime(discs) {
  let t = 0;
  let step = 1;

  discs.forEach(([positions, startPos], i) => {
    let discIndex = i + 1;
    while ((startPos + t + discIndex) % positions !== 0) t += step;
    step *= positions / gcd(step, positions);
  });

  return t;
}

function gcd(a, b) {
  while (b !== 0) [a, b] = [b, a % b];
  return a;
}

module.exports = { findFirstValidTime, parseInput };

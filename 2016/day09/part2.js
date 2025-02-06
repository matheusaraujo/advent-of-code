function part2(puzzleInput) {
  let count = 0;
  for (let line of puzzleInput) {
    count += countCharsRecursive(line);
  }
  return count;
}

function countCharsRecursive(subs) {
  let count = 0;
  let i = 0;

  while (i < subs.length) {
    if (subs[i] !== "(") {
      count += 1;
      i += 1;
    } else {
      let match = subs.slice(i).match(/^\((\d+)x(\d+)\)/);
      if (!match) {
        count += 1;
        i += 1;
      } else {
        let [fullMatch, chars, repeat] = match;
        chars = parseInt(chars, 10);
        repeat = parseInt(repeat, 10);
        let markerLength = fullMatch.length;
        let segment = subs.slice(i + markerLength, i + markerLength + chars);
        count += countCharsRecursive(segment) * repeat;
        i += markerLength + chars;
      }
    }
  }
  return count;
}

module.exports = part2;

function part1(puzzleInput) {
  return puzzleInput.filter(supportsTls).length;
}

function supportsTls(ip) {
  const parts = ip.split(/\[|\]/);
  let supportsTls = false;

  for (let i = 0; i < parts.length; i++) {
    if (i % 2 === 0 && isAbba(parts[i])) {
      supportsTls = true;
    } else if (isAbba(parts[i])) {
      return false;
    }
  }
  return supportsTls;
}

function isAbba(str) {
  for (let i = 0; i < str.length - 3; i++) {
    if (
      str[i] === str[i + 3] &&
      str[i + 1] === str[i + 2] &&
      str[i] !== str[i + 1]
    ) {
      return true;
    }
  }
  return false;
}

module.exports = part1;

const crypto = require("crypto");

function part1(puzzleInput) {
  const doorId = puzzleInput[0];
  let password = "",
    index = 0;

  while (password.length < 8) {
    const hash = crypto
      .createHash("md5")
      .update(`${doorId}${index++}`)
      .digest("hex");
    if (hash.startsWith("00000")) password += hash[5];
  }

  return password;
}

module.exports = part1;

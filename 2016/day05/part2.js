const crypto = require("crypto");

function part2(puzzleInput) {
  const doorId = puzzleInput[0];
  let password = ["_", "_", "_", "_", "_", "_", "_", "_"];
  let index = 0,
    filledPositions = 0;

  while (filledPositions < 8) {
    const hash = crypto
      .createHash("md5")
      .update(`${doorId}${index}`)
      .digest("hex");

    if (hash.startsWith("00000")) {
      let pos = hash[5];
      if (pos >= "0" && pos <= "7") {
        pos = parseInt(pos);
        if (password[pos] === "_") {
          password[pos] = hash[6];
          filledPositions++;
        }
      }
    }

    index++;
  }

  return password.join("");
}

module.exports = part2;

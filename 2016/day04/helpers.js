function Room(line) {
  this.line = line;

  const parts = line.split("-");
  const letters = parts.slice(0, -1).join("-");
  const [sectorId, checksum] = parts[parts.length - 1].split("[");

  this.letters = letters;
  this.sectorId = parseInt(sectorId);
  this.checksum = checksum.slice(0, -1);
}

Room.prototype.isReal = function () {
  const charCount = {};
  for (const char of this.letters) {
    if (char === "-") {
      continue;
    }
    charCount[char] = (charCount[char] || 0) + 1;
  }

  const sortedChars = Object.keys(charCount).sort((a, b) => {
    if (charCount[b] === charCount[a]) {
      return a.localeCompare(b);
    }
    return charCount[b] - charCount[a];
  });

  return sortedChars.slice(0, 5).join("") == this.checksum;
};

Room.prototype.decrypt = function () {
  const alphabet = "abcdefghijklmnopqrstuvwxyz";
  const decrypted = this.letters.split("").map((char) => {
    if (char === "-") {
      return " ";
    }
    return alphabet[(alphabet.indexOf(char) + this.sectorId) % alphabet.length];
  });
  return decrypted.join("");
};

module.exports = Room;

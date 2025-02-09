const crypto = require("crypto");

function findKeyIndex(salt, num, hashCount = 1) {
  const hashes = [];
  const candidates = [];
  const keys = [];

  for (let i = 0; keys.length < 64; i++) {
    let hash = salt + i;
    for (let x = 0; x < hashCount; x++)
      hash = crypto.createHash("md5").update(hash).digest("hex");

    hashes[i] = hash;

    let match;
    if ((match = hash.match(/(.)\1{2}/)))
      candidates[i] = { i, hash, c: match[1] };

    const candidate = candidates[i - 1000];
    if (candidate) {
      const matches = hashes
        .slice(i - 999)
        .filter((h) => new RegExp(`${candidate.c}{5}`).test(h));
      if (matches.length) keys.push(candidate.i);
    }
  }
  return keys[num - 1];
}

module.exports = findKeyIndex;

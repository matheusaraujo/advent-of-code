function part2(puzzleInput) {
  return puzzleInput.filter(supportsSsl).length;
}

function supportsSsl(ip) {
  const parts = ip.split(/\[|\]/);
  let abas = [];
  let babs = [];

  parts.forEach((part, index) => {
    for (let j = 0; j < part.length - 2; j++) {
      if (part[j] === part[j + 2] && part[j] !== part[j + 1]) {
        if (index % 2 === 0) abas.push(part.slice(j, j + 3));
        else babs.push(part.slice(j, j + 3));
      }
    }
  });

  return abas.some((aba) => babs.includes(`${aba[1]}${aba[0]}${aba[1]}`));
}

module.exports = part2;

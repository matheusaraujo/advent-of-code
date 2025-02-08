function parseInput(puzzleInput) {
  const floors = new Array(4).fill(null);
  const floorNum = { first: 0, second: 1, third: 2, fourth: 3 };
  const materialNum = {};
  let materialCount = 0;

  for (const line of puzzleInput) {
    const floorName = /^The (\w+) floor contains/.exec(line)[1];
    const chips = [...line.matchAll(/a (\w+)-compatible microchip/g)].map(
      (m) => m[1],
    );
    const gens = [...line.matchAll(/a (\w+) generator/g)].map((m) => m[1]);
    const floor = floorNum[floorName];

    for (const item of chips.concat(gens)) {
      if (!(item in materialNum)) {
        materialNum[item] = materialCount++;
      }
    }

    floors[floor] = [
      chips.map((c) => materialNum[c]),
      gens.map((g) => materialNum[g]),
    ];
  }

  return { floors, materialCount };
}

function solve(state) {
  const seen = new Set();
  const queue = [[0, state]];
  while (queue.length > 0) {
    const [i, state] = queue.shift();
    if (isSolved(state)) return i;

    seen.add(key(state));
    const [e] = state;
    const moves = possibleMoves(state, e + 1).concat(
      possibleMoves(state, e - 1),
    );
    for (const s of moves) {
      const k = key(s);
      if (!seen.has(k)) {
        queue.push([i + 1, s]);
        seen.add(k);
      }
    }
  }
  return -1;
}

function isSolved(state) {
  const [, floors] = state;
  return floors.slice(0, 3).every(([c, g]) => c.length + g.length === 0);
}

function key(state) {
  const [e, floors] = state;
  return `${e}:${floors.map(([c, g]) => `${c.length},${g.length}`).join("|")}`;
}

function possibleMoves(state, dest) {
  const [e, floors] = state;
  if (dest >= 0 && dest <= 3) {
    const [srcChips, srcGens] = floors[e];
    const chips = [[]].concat(combinations(srcChips, 1));
    const gens = [[]].concat(combinations(srcGens, 1));
    if (dest > e) {
      chips.push(...combinations(srcChips, 2));
      gens.push(...combinations(srcGens, 2));
    }
    const moves = product(chips, gens)
      .filter(([c, g]) => c.length + g.length > 0 && c.length + g.length <= 2)
      .map(([c, g]) => move(state, dest, c, g));
    return moves.filter((m) => isValid(m));
  } else {
    return [];
  }
}

function move(state, dest, chips, gens) {
  const [e, floors] = state;
  const newFloors = new Array(4);
  for (let i = 0; i < 4; i++) {
    const [floorChips, floorGens] = floors[i];
    if (i === e)
      newFloors[i] = [
        floorChips.filter((c) => !chips.includes(c)),
        floorGens.filter((g) => !gens.includes(g)),
      ];
    else if (i === dest)
      newFloors[i] = [
        [...floorChips, ...chips],
        [...floorGens, ...gens],
      ];
    else newFloors[i] = [floorChips, floorGens];
  }
  return [dest, newFloors];
}

function isValid(state) {
  const [, floors] = state;
  for (const [chips, gens] of floors) {
    if (gens.length > 0 && chips.some((chip) => !gens.includes(chip)))
      return false;
  }
  return true;
}

function combinations(arr, k) {
  if (k > arr.length || k <= 0) return [];
  if (k === arr.length) return [arr];
  if (k === 1) return arr.map((e) => [e]);

  const combs = [];
  for (let i = 0; i <= arr.length - k; i++) {
    const head = arr.slice(i, i + 1);
    const tail = combinations(arr.slice(i + 1), k - 1);
    tail.forEach((t) => combs.push(head.concat(t)));
  }
  return combs;
}

function product(arr1, arr2) {
  const result = [];
  for (const a of arr1) {
    for (const b of arr2) {
      result.push([a, b]);
    }
  }
  return result;
}

module.exports = { parseInput, solve };

function swapCard(operations) {
  const WIDTH = 50,
    HEIGHT = 6;
  const screen = Array.from({ length: HEIGHT }, () => Array(WIDTH).fill("."));

  for (const operation of operations) {
    const numbers = operation.match(/\d+/g).map(Number);

    if (operation.startsWith("rect")) {
      createRect(screen, numbers[0], numbers[1]);
    } else if (operation.startsWith("rotate row")) {
      rotateRow(screen, numbers[0], numbers[1]);
    } else if (operation.startsWith("rotate column")) {
      rotateColumn(screen, numbers[0], numbers[1]);
    }
  }

  return screen;
}

function createRect(screen, width, height) {
  for (let row = 0; row < height; row++) {
    for (let col = 0; col < width; col++) {
      screen[row][col] = "#";
    }
  }
}

function rotateRow(screen, row, shift) {
  screen[row] = [...screen[row].slice(-shift), ...screen[row].slice(0, -shift)];
}

function rotateColumn(screen, col, shift) {
  const height = screen.length;
  const column = screen.map((row) => row[col]);
  const rotated = column.map((_, i, arr) => arr[(i - shift + height) % height]);
  screen.forEach((row, i) => (row[col] = rotated[i]));
}

const LETTERS = {
  "####.#....###..#....#....####.": "E",
  "####.#....###..#....#....#....": "F",
  "#...##...#.#.#...#....#....#..": "Y",
  "#..#.#.#..##...#.#..#.#..#..#.": "K",
  "###..#..#.#..#.###..#.#..#..#.": "R",
  ".###...#....#....#....#...###.": "I",
  "..##....#....#....#.#..#..##..": "J",
};

function decodeScreen(screen) {
  let result = "";
  for (let col = 0; col < screen[0].length; col += 5) {
    let pattern = screen
      .map((row) => row.slice(col, col + 5).join(""))
      .join("");
    result += LETTERS[pattern] || "?";
  }
  return result;
}

module.exports = { swapCard, decodeScreen };

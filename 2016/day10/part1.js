const { parseInstructions, processBots } = require("./helpers");

function part1(puzzleInput) {
  const { botChips, botRules } = parseInstructions(puzzleInput);
  const { targetBot } = processBots(botChips, botRules, [17, 61]);
  return targetBot;
}

module.exports = part1;

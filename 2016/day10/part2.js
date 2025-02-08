const { parseInstructions, processBots } = require("./helpers");

function part2(puzzleInput) {
  const { botChips, botRules } = parseInstructions(puzzleInput);
  const { outputs } = processBots(botChips, botRules, [17, 61]);
  return outputs[0] * outputs[1] * outputs[2];
}

module.exports = part2;

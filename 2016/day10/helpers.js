function parseInstructions(instructions) {
  const botChips = new Map();
  const botRules = new Map();

  instructions.forEach((line) => {
    const parts = line.split(" ");
    if (parts[0] === "value") {
      const value = parseInt(parts[1]);
      const bot = parseInt(parts[5]);
      if (!botChips.has(bot)) botChips.set(bot, []);
      botChips.get(bot).push(value);
    } else {
      const bot = parseInt(parts[1]);
      const lowTarget = [parts[5], parseInt(parts[6])];
      const highTarget = [parts[10], parseInt(parts[11])];
      botRules.set(bot, [lowTarget, highTarget]);
    }
  });

  return { botChips, botRules };
}

function processBots(botChips, botRules, targetPair) {
  const queue = [...botChips.keys()].filter(
    (bot) => botChips.get(bot).length === 2,
  );
  const outputs = {};
  let targetBot = null;

  while (queue.length > 0) {
    const bot = queue.shift();
    const chips = botChips.get(bot).sort((a, b) => a - b);

    if (chips[0] === targetPair[0] && chips[1] === targetPair[1]) {
      targetBot = bot;
    }

    const [lowChip, highChip] = chips;
    const [lowTarget, highTarget] = botRules.get(bot);

    [
      [lowChip, lowTarget],
      [highChip, highTarget],
    ].forEach(([chip, target]) => {
      const [type, num] = target;
      if (type === "bot") {
        if (!botChips.has(num)) botChips.set(num, []);
        botChips.get(num).push(chip);
        if (botChips.get(num).length === 2) queue.push(num);
      } else {
        outputs[num] = chip;
      }
    });

    botChips.set(bot, []);
  }

  return { targetBot, outputs };
}

module.exports = { parseInstructions, processBots };

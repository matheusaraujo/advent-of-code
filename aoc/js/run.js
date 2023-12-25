const fs = require('fs');
const part1 = require("../../2015/day01/part1")
const part2 = require("../../2015/day01/part2")
const assert = require('assert');

const formatTime = function(executionTime) {
    return (executionTime).toFixed(2) + "ms"
}

const data = JSON.parse(fs.readFileSync('data/2015-01.json', 'utf8'));

console.log(`javascript: Running AOC ${data.year} Day ${data.day} - ${data.title}`)

const input = fs.readFileSync(data.input_file, 'utf8')

const expectedOutputPar1 = fs.readFileSync(data.part1.output_file, 'utf8')
const startTime1 = performance.now();
const answer1 = part1(input)
const endTime1 = performance.now();
const executionTime1 = endTime1 - startTime1;
console.log("\033[35mPart 1: \033[32m" + answer1 + "\033[3;90m (executed in " + formatTime(executionTime1) + ") \033[0m")
assert.equal(answer1, expectedOutputPar1)

const expectedOutputPar2 = fs.readFileSync(data.part2.output_file, 'utf8')
const startTime2 = performance.now();
const answer2 = part2(input)
const endTime2 = performance.now();
const executionTime2 = endTime2 - startTime2;
console.log("\033[35mPart 2: \033[32m" + answer2 + "\033[3;90m (executed in " + formatTime(executionTime2) + ") \033[0m")
assert.equal(answer2, expectedOutputPar2)


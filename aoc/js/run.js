const fs = require('fs');
const part1 = require("../../2015/day01/part1")
const assert = require('assert');

const data = JSON.parse(fs.readFileSync('data/2015-01.json', 'utf8'));


const input = fs.readFileSync(data.input_file, 'utf8')
const expectedOutput = fs.readFileSync(data.part1.output_file, 'utf8')

const answer = part1(input)

assert.equal(answer, expectedOutput)


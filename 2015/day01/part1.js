process.stdin.setEncoding('utf8');

function countOccurrences(str, char) {
    return str.split(char).length - 1;
}

function part1(data) {
    return countOccurrences(data, "(") - countOccurrences(data, ")")
}

process.stdin.on('data', function (data) {
  console.log(part1(data.trim()));
});


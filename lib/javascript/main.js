const fs = require('fs');

const [,, year, day, part] = process.argv;

let func = require(`../../${year}/day${day}/${part}.js`);

function main() {
  const input_data = fs.readFileSync(0, 'utf-8');
  console.log(func(input_data));
}

main();

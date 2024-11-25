#!/bin/bash

year=$1
day=$2

curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//') -o $year/day$day/_readme1.html

if ! grep -q '<p class="day-success">Both parts of this puzzle are complete!' $year/day$day/_readme1.html; then
  echo "puzzle is not complete yet"
  exit 1
fi

sed -n '/<main>/,/<\/main>/p' $year/day$day/_readme1.html > $year/day$day/_readme2.html
sed '/<p class="day-success">Both parts of this puzzle are complete!/q' $year/day$day/_readme2.html | sed '$a</main>' > $year/day$day/_readme3.html

pandoc --from=html --to=markdown --output=$year/day$day/README.md $year/day$day/_readme3.html

sed -i 's/::: {role="main"}//g' $year/day$day/README.md
sed -i 's/{#part2}//g' $year/day$day/README.md
sed -i '${/^:::$/d}' $year/day$day/README.md

rm $year/day$day/_readme*.html

echo -e "readme $year/day$day generated \033[32m✔\033[0m"

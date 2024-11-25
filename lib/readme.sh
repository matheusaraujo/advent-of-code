#!/bin/bash

year=$1
day=$2

# Fetch the HTML content
curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//') -o $year/day$day/_readme1.html

# Check if the "day-success" paragraph exists
if ! grep -q '<p class="day-success">Both parts of this puzzle are complete!' $year/day$day/_readme1.html; then
  echo "Error: Puzzle is not marked as complete. Exiting."
  exit 1
fi

# Extract <main> content and clean up
sed -n '/<main>/,/<\/main>/p' $year/day$day/_readme1.html > $year/day$day/_readme2.html
sed '/<p class="day-success">Both parts of this puzzle are complete!/q' $year/day$day/_readme2.html | sed '$a</main>' > $year/day$day/_readme3.html

# Convert to Markdown
pandoc --from=html --to=markdown --output=$year/day$day/README.md $year/day$day/_readme3.html

# Post-process the Markdown to remove unwanted substrings
sed -i 's/::: {role="main"}//g' $year/day$day/README.md  # Remove "::: {role=\"main\"}"
sed -i 's/{#part2}//g' $year/day$day/README.md           # Remove "{#part2}"
sed -i '${/^:::$/d}' $year/day$day/README.md            # Remove trailing ":::"

# Clean up temporary files
rm $year/day$day/_readme*.html

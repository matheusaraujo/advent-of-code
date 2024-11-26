#!/bin/bash

year=$1
day=$2

readme_path="$year/day$day/README.md"

if [ ! -f "$readme_path" ]; then
    echo "Error: README.md file does not exist at $readme_path"
    exit 1
fi

puzzle_title=$(head -2 "$readme_path" | tail -1 | sed 's/^.\{6\}//; s/.\{6\}$//' | xargs)

if [ -z "$puzzle_title" ]; then
    echo "Error: Unable to extract puzzle title from $readme_path"
    exit 1
fi

git add "README.md"
git add "$year/day$day"
git commit -m "feat($year): $puzzle_title"

echo -e "code commited! \033[32m✔\033[0m"
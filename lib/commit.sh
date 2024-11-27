#!/bin/bash

year=$1
day=$2

readme_path="$year/day$day/README.md"
puzzle_folder="$year/day$day"

if [ ! -f "$readme_path" ]; then
    echo "Error: README.md file does not exist at $readme_path"
    exit 1
fi

puzzle_title=$(head -2 "$readme_path" | tail -1 | sed 's/^.\{6\}//; s/.\{6\}$//' | xargs)

if [ -z "$puzzle_title" ]; then
    echo "Error: Unable to extract puzzle title from $readme_path"
    exit 1
fi

changed_files=($(git status --porcelain | awk '{print $2}'))
if [[ ${#changed_files[@]} -ne 2 || "${changed_files[0]}" != "$readme_path" || "${changed_files[1]}" != "$puzzle_folder" ]]; then
    echo "Error: Unexpected changes detected. Expected only:"
    echo "1. $readme_path"
    echo "2. $puzzle_folder"
    exit 1
fi

git add "$readme_path"
git add "$puzzle_folder"
git commit -m "feat($year): $puzzle_title"

echo -e "code committed! \033[32m✔\033[0m"

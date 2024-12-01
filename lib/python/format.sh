#!/bin/bash

year=$1
day=$2

if [ -f "$year/day$day/requirements.txt" ]; then
    pip install -q -r "$year/day$day/requirements.txt"
fi

files=("part1.py" "part2.py" "helpers.py" "utils.py")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        isort $year/day$day/$file && echo -e "isort $year/day$day/$file \033[32m✔\033[0m"
        black $year/day$day/$file -l 88 -q && echo -e "black $year/day$day/$file \033[32m✔\033[0m"
    fi
done

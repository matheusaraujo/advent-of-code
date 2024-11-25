#!/bin/bash

year=$1
day=$2

files=("part1.pl" "part2.pl")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        perltidy -b $year/day$day/$file && echo -e "perltidy $year/day$day/$file \033[32m✔\033[0m"
    fi
done

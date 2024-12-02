#!/bin/bash

year=$1
day=$2

files=("part1.c" "part2.c" "helpers.c")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        clang-format -i $year/day$day/$file && echo -e "clang-format $year/day$day/$file \033[32m✔\033[0m"
    fi
done

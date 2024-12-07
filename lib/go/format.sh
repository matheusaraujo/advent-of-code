#!/bin/bash

year=$1
day=$2

files=("part1.go" "part2.go" "helpers.go")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        gofmt -w $year/day$day/$file && echo -e "gofmt $year/day$day/$file \033[32m✔\033[0m"
    fi
done

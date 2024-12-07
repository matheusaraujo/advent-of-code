#!/bin/bash

year=$1
day=$2

files=("$year/day$day/part1.go")

if [ -f "$year/day$day/helpers.go" ]; then
    files+=("$year/day$day/helpers.go")
fi

if [ -f "$year/day$day/part2.go" ]; then
    files+=("$year/day$day/part2.go")
fi

output=$(go vet "${files[@]}" 2>&1)

if [ $? -ne 0 ]; then
    echo "go vet failed for $year/day$day/"
    echo "$output"
    exit 1
else
    echo -e "go vet $year/day$day/ \033[32m✔\033[0m"
fi

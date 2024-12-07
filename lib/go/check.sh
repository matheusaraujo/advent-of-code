#!/bin/bash

year=$1
day=$2

files=("part1.go" "part2.go" "helpers.go")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        output=$(go vet "$year/day$day/$file" 2>&1)
        if [ $? -ne 0 ]; then
            echo "go vet failed for $year/day$day/$file"
            echo "$output"
            exit 1
        else
            echo -e "go vet $year/day$day/$file \033[32m✔\033[0m"
        fi
    fi
done

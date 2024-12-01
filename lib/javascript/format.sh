#!/bin/bash

source lib/aoc/utils.sh

year=$1
day=$2

files=("part1.js" "part2.js" "helpers.js")

npm --silent --prefix lib/javascript/ install lib/javascript/

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        if prettier "$year/day$day/$file" --write --log-level silent; then
            print_success "prettier $year/day$day/$file \033[32m✔\033[0m"
        else
            exit 1
        fi
    fi
done
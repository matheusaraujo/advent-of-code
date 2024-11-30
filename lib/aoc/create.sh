#!/bin/bash

aoc_create() {
    if ! validate_year_day_lang; then
        return 1
    fi
    
    ext=${lang_extensions[$lang]}
    mkdir -p $year/day$day/data
    cp -r 2000/day00/part1.$ext $year/day$day
    cp -r 2000/day00/part2.$ext $year/day$day
    curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//')/input -o $year/day$day/data/input.txt
    print_success "$year/day$day created using $lang! \033[32m✔\033[0m \ngood coding! 💻"
}
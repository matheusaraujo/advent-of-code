#!/bin/bash

year=$1
day=$2

files=("part1.pl" "part2.pl")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        perlcritic -b $year/day$day/$file --profile lib/perl/.perlcriticrc || exit 1
    fi
done
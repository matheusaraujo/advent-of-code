#!/bin/bash

year=$1
day=$2

if [ -f "$year/day$day/requirements.txt" ]; then
    pip install -q -r "$year/day$day/requirements.txt"
fi

files=("part1.py" "part2.py" "helpers.py")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        pylint $year/day$day/$file --rcfile=lib/python/.pylintrc || exit 1
    fi
done
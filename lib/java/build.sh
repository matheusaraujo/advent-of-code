#!/bin/bash

year=$1
day=$2

files="lib/java/main.java $year/day$day/part1.java"

helpers_file="$year/day$day/helpers.java"
if [[ -f "$helpers_file" ]]; then
    files="$files $helpers_file"
fi

part2_file="$year/day$day/part2.java"
if [[ -f "$part2_file" ]]; then
    files="$files $part2_file"
fi

javac $files

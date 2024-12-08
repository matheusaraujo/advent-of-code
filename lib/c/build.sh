#!/bin/bash

year=$1
day=$2

helpers_file=""
if [ -f "$year/day$day/helpers.c" ]; then
    helpers_file="$year/day$day/helpers.c"
fi

part2_file=""
if [ -f "$year/day$day/part2.c" ]; then
    part2_file="$year/day$day/part2.c"
fi

gcc -o lib/c/run \
    -Ilib/c \
    $helpers_file \
    lib/c/aoc_helpers.c \
    $year/day$day/part1.c \
    $part2_file \
    lib/c/main.c

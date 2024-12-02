#!/bin/bash

year=$1
day=$2
part=$3
input_file=$4

gcc -o lib/c/run \
    -Ilib/c \
    lib/c/helpers.c \
    $year/day$day/part1.c \
    $year/day$day/part2.c \
    lib/c/main.c

./lib/c/run $year $day $part < $input_file


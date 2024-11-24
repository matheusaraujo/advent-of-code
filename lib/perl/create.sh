#!/bin/bash

year=$1
day=$2

mkdir -p $year/day$day/data
cp -r 1988/day00/part1.pl $year/day$day
cp -r 1988/day00/part2.pl $year/day$day
curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//')/input -o $year/day$day/data/input.txt

echo "$year/day$day created! good coding!"
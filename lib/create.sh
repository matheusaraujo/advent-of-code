#!/bin/bash

source lib/utils.sh

year=$1
day=$2
lang=$3

ext=${lang_extensions[$lang]}

mkdir -p $year/day$day/data

cp -r 2000/day00/part1.$ext $year/day$day
cp -r 2000/day00/part2.$ext $year/day$day

curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//')/input -o $year/day$day/data/input.txt

echo -e "$year/day$day created using $lang! \033[32m✔\033[0m \ngood coding! 💻"
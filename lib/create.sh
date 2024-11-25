#!/bin/bash

year=$1
day=$2
lang=$3

mkdir -p $year/day$day/data

if [ $lang == "perl" ]; then
  lib/perl/create.sh $year $day
elif [ $lang == "python" ]; then
  lib/python/create.sh $year $day
fi

curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//')/input -o $year/day$day/data/input.txt

echo "$year/day$day created! good coding!"
#!/bin/bash

year=$1
day=$2
lang=$3

mkdir -p $year/day$day/data
lib/$lang/create.sh $year $day
curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//')/input -o $year/day$day/data/input.txt

echo "$year/day$day created using $lang! good coding!"
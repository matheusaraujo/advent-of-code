#!/bin/bash

year=$1
day=$2

isort $year/day$day/part1.py && echo -e "isort $year/day$day/part1.py \033[32m✔\033[0m"
isort $year/day$day/part2.py && echo -e "isort $year/day$day/part2.py \033[32m✔\033[0m"

black $year/day$day/part1.py -l 88 -q && echo -e "black $year/day$day/part1.py \033[32m✔\033[0m"
black $year/day$day/part2.py -l 88 -q && echo -e "black $year/day$day/part2.py \033[32m✔\033[0m"
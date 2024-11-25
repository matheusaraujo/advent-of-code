#!/bin/bash

year=$1
day=$2

perltidy -b $year/day$day/part1.pl && echo -e "perltidy -b $year/day$day/part1.pl \033[32m✔\033[0m"
perltidy -b $year/day$day/part2.pl && echo -e "perltidy -b $year/day$day/part2.pl \033[32m✔\033[0m"
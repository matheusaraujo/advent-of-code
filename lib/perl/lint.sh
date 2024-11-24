#!/bin/bash

year=$1
day=$2

perltidy -b $year/day$day/part1.pl
perltidy -b $year/day$day/part2.pl
#!/bin/bash

year=$1
day=$2

perlcritic -b $year/day$day/part1.pl
perlcritic -b $year/day$day/part2.pl
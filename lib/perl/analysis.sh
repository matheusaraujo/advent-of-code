#!/bin/bash

year=$1
day=$2

perlcritic -b $year/day$day/part1.pl --profile lib/perl/.perlcriticrc || exit 1
perlcritic -b $year/day$day/part2.pl --profile lib/perl/.perlcriticrc || exit 1
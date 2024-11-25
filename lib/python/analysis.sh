#!/bin/bash

year=$1
day=$2

pylint $year/day$day/part1.py --rcfile=lib/python/.pylintrc  || exit 1
pylint $year/day$day/part2.py --rcfile=lib/python/.pylintrc || exit 1
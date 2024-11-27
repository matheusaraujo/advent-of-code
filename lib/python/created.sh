#!/bin/bash

year=$1
day=$2

if [[ -f "$year/day$day/part1.py" ]]; then
    exit 0
else
    exit 1
fi
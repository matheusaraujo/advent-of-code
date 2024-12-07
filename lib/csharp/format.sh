#!/bin/bash

year=$1
day=$2

files=("part1.cs" "part2.cs" "helpers.cs")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        dotnet-csharpier $year/day$day/$file && echo -e "dotnet-csharpier $year/day$day/$file \033[32m✔\033[0m"
    fi
done

#!/bin/bash

year=$1
day=$2

files=("part1.java" "part2.java" "helpers.java")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        java -jar /usr/local/bin/google-java-format -i $year/day$day/$file && echo -e "google-java-format $year/day$day/$file \033[32m✔\033[0m"
    fi
done

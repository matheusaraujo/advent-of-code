#!/bin/bash

year=$1
day=$2

files=("part1.c" "part2.c" "helpers.c")

for file in "${files[@]}"; do
    if [ -f "$year/day$day/$file" ]; then
        output=$(clang --analyze -fcolor-diagnostics -Werror -Ilib/c "$year/day$day/$file" 2>&1)
        if [ -n "$output" ]; then
            echo -e "clang --analyze $year/day$day/$file \033[31m✘\033[0m"
            echo -e "$output"
            exit 1
        else
            echo -e "clang --analyze $year/day$day/$file \033[32m✔\033[0m"
        fi

        tidy_output=$(clang-tidy "$year/day$day/$file" -extra-arg=-w --quiet --use-color --config-file=lib/c/.clang-tidy -- -Ilib/c -std=c11 2>&1)
        if [[ -n "$tidy_output" && ! "$tidy_output" =~ ^[0-9]+[[:space:]]+warnings[[:space:]]+generated\.$ ]]; then
            echo -e "clang-tidy $year/day$day/$file \033[31m✘\033[0m"
            echo -e "$tidy_output"
            exit 1
        else
            echo -e "clang-tidy $year/day$day/$file \033[32m✔\033[0m"
        fi
    fi
done

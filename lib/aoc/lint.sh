#!/bin/bash

aoc_lint() {
    if ! validate_year_day; then
        return 1
    fi
    
    for lang in python perl; do
        
        local ext=${lang_extensions[$lang]}

        if [ -f "$year/day$day/part1.$ext" ]; then
            echo "lint($lang): AoC $year - Day $day"
            lib/$lang/lint.sh $year $day

            if [ $? -ne 0 ]; then
                exit 1
            fi
        fi
    done
}
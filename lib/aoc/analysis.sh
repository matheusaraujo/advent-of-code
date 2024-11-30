#!/bin/bash

aoc_analysis() {
    validate_year_day_directory
    
    for lang in "${languages[@]}"; do
        local ext=${lang_extensions[$lang]}

        if [ -f "$year/day$day/part1.$ext" ]; then
            print_success "analysis($lang): AoC $year - Day $day"
            lib/$lang/analysis.sh $year $day

            if [ $? -ne 0 ]; then
                exit 1
            fi
        fi
    done
}
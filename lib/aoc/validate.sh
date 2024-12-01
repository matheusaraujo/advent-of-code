#!/bin/bash

aoc_validate() {
    validate_year_day_directory
    
    for lang in "${available_languages[@]}"; do
        local ext=${language_extensions[$lang]}

        if [ -f "$year/day$day/part1.$ext" ]; then
            print_success "validate($lang): AoC $year - Day $day"
            lib/$lang/validate.sh $year $day

            if [ $? -ne 0 ]; then
                exit 1
            fi
        fi
    done
}
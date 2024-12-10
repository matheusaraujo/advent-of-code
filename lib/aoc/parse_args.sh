#!/bin/bash

update_aoc_env() {
    local key="$1"
    local value="$2"

    if [[ ! -f .aoc-env ]]; then
        echo "$key=$value" >> .aoc-env
    else
        if grep -q "^$key=" .aoc-env; then
            sed -i "/^$key=/c\\$key=$value" .aoc-env
        else
            echo "$key=$value" >> .aoc-env
        fi
    fi
}

infer_year_day(){
    rm -rf .aoc-env
    if [ "$(date +%m%d)" -ge "1201" ] && [ "$(date +%m%d)" -le "1225" ]; then
        year=$(date +%Y)
        day=$(date +%d)
        update_aoc_env "year" "$year"
        update_aoc_env "day" "$day"
    fi
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        if [[ $1 =~ ^[2][0][1-9][5-9]$ || $1 =~ ^[2][0][2][0-4]$ ]]; then
            year="$1"
            update_aoc_env "year" "$year"
        elif [[ $1 =~ ^([1-9]|0[0-9]|1[0-9]|2[0-5])$  ]]; then
            arg=$(echo "$1" | sed 's/^0*//')
            day=$(printf "%02d" "$arg")
            update_aoc_env "day" "$day"
        elif [[ $1 == "part1" || $1 == "part2" ]]; then
            part="$1"
        elif [[ " ${!language_aliases[@]} " =~ " $1 " ]]; then
            lang="${language_aliases[$1]}"
        elif [[ $1 == "--watch" || $1 == "-w" ]]; then
            watch_mode="true"
        else
            print_error "Unknown option: $1"
            exit 1
        fi
        shift
    done

    if [[ -z "$year" && -z "$day" && -f ".aoc-env" ]]; then
        source .aoc-env
    fi
}

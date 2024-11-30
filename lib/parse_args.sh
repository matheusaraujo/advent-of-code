#!/bin/bash

parse_args() {
    while [[ $# -gt 0 ]]; do
        if [[ $1 =~ ^[2][0][1-9][5-9]$ || $1 =~ ^[2][0][2][0-4]$ ]]; then
            year="$1"
        elif [[ $1 =~ ^[0-9]{1,2}$ && $1 -ge 1 && $1 -le 25 ]]; then 
            day=$(printf "%02d" $1)
        elif [[ $1 == "part1" || $1 == "part2" ]]; then
            part="$1"
        elif [[ $1 == "python" || $1 == "perl" ]]; then
            lang="$1"
        elif [[ $1 == "--watch" || $1 == "-w" ]]; then
            watch_mode="true"
        else
            echo "Unknown option: $1"
            exit 1
        fi
        shift
    done
}
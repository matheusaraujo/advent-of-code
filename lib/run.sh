#!/bin/bash

year=$1
day=$2
#part=$3
#test=$4

echo "perl: AoC $year - Day $day"

run_part() {
    part=$1
    input_files=$(ls "$year/day$day/data/input.$part"*)

    for input_file in $input_files; do
        output_file=$(echo "$input_file" | sed 's/input/output/')
        if [ ! -f "$output_file" ]; then
            echo "Error: Output file $output_file does not exist."
            exit 1
        fi  
        lib/perl/run.sh $year $day $part "$input_file" "$output_file"
    done

    if [ -f "$year/day$day/data/output.$part.txt" ]; then
        lib/perl/run.sh $year $day $part "$year/day$day/data/input.txt"  "$year/day$day/data/output.$part.txt"
    else  
        lib/perl/run.sh $year $day $part "$year/day$day/data/input.txt"
    fi
}

run_part "part1"
run_part "part2"

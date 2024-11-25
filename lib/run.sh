#!/bin/bash

year=$1
day=$2

run() {
    lang=$1
    part=$2
    
    input_files=$(ls "$year/day$day/data/input.$part"* 2>/dev/null)

    if [ -n "$input_files" ]; then
        for input_file in $input_files; do
            output_file=$(echo "$input_file" | sed 's/input/output/')
            if [ ! -f "$output_file" ]; then
                echo "Error: Output file $output_file does not exist."
                exit 1
            fi  
            lib/$lang/run.sh $year $day $part "$input_file" "$output_file"

            if [ $? -ne 0 ]; then
                exit 1
            fi
        done
    fi

    if [ -f "$year/day$day/data/output.$part.txt" ]; then
        lib/$lang/run.sh $year $day $part "$year/day$day/data/input.txt"  "$year/day$day/data/output.$part.txt"
    else  
        lib/$lang/run.sh $year $day $part "$year/day$day/data/input.txt"
    fi

    if [ $? -ne 0 ]; then
        exit 1
    fi
}

for lang in python perl; do
    lib/$lang/created.sh $year $day
    if [ $? -eq 0 ]; then
        echo "$lang: AoC $year - Day $day"
        run "$lang" "part1"
        run "$lang" "part2"
    fi
done

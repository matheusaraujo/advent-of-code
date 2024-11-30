#!/bin/bash

year=$1
day=$2

declare -A lang_extensions
lang_extensions=(
    ["perl"]="pl"
    ["python"]="py"
)

get_input_file_label() {
    file_name=$(basename "$1")
    if [ "$file_name" == "input.txt" ]; then
        echo ""
    else
        IFS='.' read -ra parts <<< "$file_name"
        label="(${parts[-2]})"
        echo "$label"
    fi
}

run_lang() {
    lang=$1
    year=$2
    day=$3
    part=$4
    input_file=$5
    output_file=$6

    start_time=$(date +%s%3N)

    script_output=$(lib/$lang/run.sh "$year" "$day" "$part" "$input_file")
    if [ $? -ne 0 ]; then
        exit 1
    fi

    end_time=$(date +%s%3N)
    elapsed_time=$((end_time - start_time))

    if [ -n "$output_file" ]; then
        if [ ! -f "$output_file" ]; then
            echo "Error: Output file $output_file does not exist."
            exit 1
        fi

        expected_output=$(cat "$output_file")

        if [ "$script_output" != "$expected_output" ]; then
            echo -e "\033[35m$part$input_label: \033[0m\033[32m$script_output\033[3;90m (executed in ${elapsed_time}ms)\033[91m ✘ Expected: $expected_output \033[0m"
            exit 1
        else
            result_symbol="\033[32m✔\033[0m"
        fi
    else
        result_symbol=""
    fi

    input_label=$(get_input_file_label "$input_file")
    echo -e "\033[35m$part$input_label: \033[0m\033[32m$script_output\033[3;90m (executed in ${elapsed_time}ms) $result_symbol\033[0m"
}

run() {
    lang=$1
    part=$2

    input_files=$(ls "$year/day$day/data/input.$part"* 2>/dev/null)

    for input_file in $input_files; do
        output_file="${input_file/input/output}"
        
        if [ ! -f "$output_file" ]; then
            echo "Error: Output file $output_file does not exist."
            exit 1
        fi
        
        run_lang $lang $year $day $part "$input_file" "$output_file"
    done

    output_txt="$year/day$day/data/output.$part.txt"
    if [ -f "$output_txt" ]; then
        run_lang $lang $year $day $part "$year/day$day/data/input.txt" "$output_txt"
    else
        run_lang $lang $year $day $part "$year/day$day/data/input.txt" ""
    fi
}



for lang in python perl; do
    ext=${lang_extensions[$lang]}

    if [ -f "$year/day$day/part1.$ext" ]; then
        echo "$lang: AoC $year - Day $day"
        
        run "$lang" "part1"

        part2_file="$year/day$day/part2.$ext"
        if [ -f "$part2_file" ]; then
            run "$lang" "part2"
        fi
    fi
done

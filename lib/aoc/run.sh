#!/bin/bash

aoc_run() {
    validate_year_day_directory
    
    if [ "$watch_mode" == "true" ]; then
        run_watch_mode
    else
        run_full_puzzle
    fi
}

run_watch_mode() {
    local watch_dir="$year/day$day"
    print_error "${GREEN}Running $watch_dir in watch mode...\nPress Ctrl+C to stop.${NC}"
    (run_full_puzzle) || true

    inotifywait -m -r -e close_write,create,delete "$watch_dir" --exclude '\.pyc(\..*)?$|\.bak$' 2>/dev/null |
    while read -r directory events filename; do
        clear
        (run_full_puzzle) || true
        print_success "\n${GREEN}Running $watch_dir in watch mode...\nPress Ctrl+C to stop.${NC}"
    done
}

run_full_puzzle() {
    for lang in "${languages[@]}"; do
        process_language_puzzle "$lang"
    done
}

process_language_puzzle() {
    local lang=$1
    local ext=${lang_extensions[$lang]}

    if [ -f "$year/day$day/part1.$ext" ]; then
        print_success "$lang: AoC $year - Day $day"

        process_language_part "$lang" "part1"

        if [ -f "$year/day$day/part2.$ext" ]; then
            process_language_part "$lang" "part2"
        fi
    fi
}

process_language_part() {
    local lang=$1
    local part=$2

    for input_file in "$year/day$day/data/input.$part"*; do
        [ -f "$input_file" ] || continue

        local output_file="${input_file/input/output}"
        validate_output_file "$output_file"

        execute_solution_script "$lang" "$year" "$day" "$part" "$input_file" "$output_file"
    done

    local input_file="$year/day$day/data/input.txt"
    local output_file="$year/day$day/data/output.$part.txt"
    if [ -f "$output_file" ]; then
        execute_solution_script "$lang" "$year" "$day" "$part" "$year/day$day/data/input.txt" $output_file
    else
        execute_solution_script "$lang" "$year" "$day" "$part" "$year/day$day/data/input.txt"
    fi
}

execute_solution_script() {
    local lang=$1
    local year=$2
    local day=$3
    local part=$4
    local input_file=$5
    local output_file=$6

    local start_time=$(date +%s%3N)
    local script_output=$(lib/$lang/run.sh "$year" "$day" "$part" "$input_file")

    if [ $? -ne 0 ]; then
        exit 1
    fi

    local end_time=$(date +%s%3N)
    local elapsed_time=$((end_time - start_time))
    local result_symbol=""
    local input_label=$(generate_input_label "$input_file")

    if [ -n "$output_file" ]; then
        validate_output_file "$output_file"
        local expected_output=$(cat "$output_file")

        if [ "$script_output" != "$expected_output" ]; then
            print_success "\033[35m$part$input_label: \033[0m\033[32m$script_output\033[3;90m (executed in ${elapsed_time}ms)\033[91m ✘ Expected: $expected_output \033[0m"
            exit 1
        fi
        result_symbol="\033[32m✔\033[0m"
    fi

    print_success "\033[35m$part$input_label: \033[0m\033[32m$script_output\033[3;90m (executed in ${elapsed_time}ms) $result_symbol\033[0m"
}

validate_output_file() {
    local output_file=$1
    if [ ! -f "$output_file" ]; then
        print_success "Error: Output file $output_file does not exist."
        exit 1
    fi
}

generate_input_label() {
    local file_name=$(basename "$1")
    if [ "$file_name" == "input.txt" ]; then
        echo ""
    else
        IFS='.' read -ra parts <<< "$file_name"
        echo "(${parts[-2]})"
    fi
}

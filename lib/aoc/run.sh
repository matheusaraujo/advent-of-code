#!/bin/bash

aoc_run() {
    validate_year_day_directory
    ensure_input_file_exists

    if [ "$watch_mode" == "true" ]; then
        run_watch_mode
    else
        run_full_puzzle
    fi
}

ensure_input_file_exists() {
    if [ ! -f "$year/day$day/data/input.txt" ]; then
        curl -s -b session=$(cat session.cookie) https://adventofcode.com/$year/day/$(echo $day | sed 's/^0*//')/input -o $year/day$day/data/input.txt
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
    for lang in "${available_languages[@]}"; do
        process_language_puzzle "$lang"
    done
}

process_language_puzzle() {
    local lang=$1
    local ext=${language_extensions[$lang]}

    if [ -f "$year/day$day/part1.$ext" ]; then
        print_success "$lang: AoC $year - Day $day"

        if [ -f "lib/$lang/build.sh" ]; then
            lib/$lang/build.sh "$year" "$day"

            if [ $? -ne 0 ]; then
                exit 1
            fi
        fi

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

    local start_time=$(date +%s%N)

    /usr/bin/time -f "Max Memory: %M KB\nCPU Usage: %P" \
        -o /tmp/resource_usage.txt -- \
        lib/$lang/run.sh "$year" "$day" "$part" "$input_file" > /tmp/script_output.txt 2>&1
    local script_exit_code=$?
    local end_time=$(date +%s%N)

    local elapsed_time=$((end_time - start_time))
    local elapsed=""
    local elapsed_ms=$(echo "scale=3; $elapsed_time / 1000000" | bc)
    local elapsed_s=$(echo "scale=3; $elapsed_time / 1000000000" | bc)
    local elapsed_min=$(echo "scale=3; $elapsed_time / 60000000000" | bc)

    if (( $(echo "$elapsed_time < 1000000000" | bc -l) )); then
        elapsed="${elapsed_ms}ms"
    elif (( $(echo "$elapsed_time < 60000000000" | bc -l) )); then
        elapsed="${elapsed_s}s"
    else
        elapsed="${elapsed_min}min"
    fi

    if [ $script_exit_code -ne 0 ]; then
        echo "Script failed to execute." >&2
        cat /tmp/script_output.txt >&2
        exit 1
    fi

    local script_output=$(cat /tmp/script_output.txt)
    local resource_usage=$(cat /tmp/resource_usage.txt)
    local max_memory_kb=$(echo "$resource_usage" | grep "Max Memory" | awk '{print $3}')
    local cpu_usage=$(echo "$resource_usage" | grep "CPU Usage" | awk '{print $3}')


    local max_memory=""
    if [ "$max_memory_kb" -ge 1048576 ]; then
        max_memory=$(echo "scale=2; $max_memory_kb / 1048576" | bc)GB
    elif [ "$max_memory_kb" -ge 1024 ]; then
        max_memory=$(echo "scale=2; $max_memory_kb / 1024" | bc)MB
    else
        max_memory="${max_memory_kb}KB"
    fi

    local result_symbol=""
    local input_label=$(generate_input_label "$input_file")

    if [ -n "$output_file" ]; then
        validate_output_file "$output_file"
        local expected_output=$(cat "$output_file")

        if [ "$script_output" != "$expected_output" ]; then
            print_error "\033[35m$part$input_label: \033[0m\033[32m$script_output\033[3;90m (execution time: ${elapsed}, memory: ${max_memory}, cpu: ${cpu_usage})\033[91m ✘ Expected: $expected_output \033[0m"
            exit 1
        fi
        result_symbol="\033[32m✔\033[0m"
    fi

    print_success "\033[35m$part$input_label: \033[0m\033[32m$script_output\033[3;90m (execution time: ${elapsed}, memory: ${max_memory}, cpu: ${cpu_usage}) $result_symbol\033[0m"
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

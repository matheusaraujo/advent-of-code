#!/bin/bash

PURPLE="\033[35m"
GREEN="\033[32m"
GREY="\033[3;90m"
RESET="\033[0m"
RED="\033[91m"

CHECK_SYMBOL="${GREEN}\xE2\x9C\x94"
CROSS_SYMBOL="${RED}\xE2\x9C\x97"

language=$1
solutions_dir=$2
json_file=$3

main() {
    if [ ! -f "$json_file" ]; then
        echo "File $json_file does not exist."
        exit 1
    fi

    part1_solved=$(jq -r ".part1.solved" "$json_file")
    part2_solved=$(jq -r ".part2.solved" "$json_file")

    if [ "$part2_solved" = "true" ]; then
        run_solved
    elif [ "$part1_solved" = "true" ]; then
        run_part2
    else
        run_part1
    fi
}

run() {
    local part=$1
    local title=$2
    local input_file=$3
    local output_file=$4

    local puzzle_input=$(<$input_file)

    if [ "$language" = "python" ]; then
        local result=$(python3 aoc/python/run2.py $part $solutions_dir $puzzle_input)
    elif [ "$language" = "js" ]; then
        local result=$(node aoc/js/run2.js $part $solutions_dir $puzzle_input)
    else
        echo "invalid language"
        exit 1
    fi

    local received_answer=$(echo "$result" | jq -r ".receivedAnswer")
    local execution_time=$(echo "$result" | jq -r ".executionTime")

    if [ -z "$4" ]; then
        printf "${PURPLE}${title} "
        printf "${GREY}(executed in ${execution_time}ms) ${RESET}"
        printf "${GREEN}${received_answer}\n"
    else
        local expected_answer=$(<$output_file)
        if [ "$received_answer" = "$expected_answer" ]; then
            printf "${PURPLE}${title} "
            printf "${GREY}(executed in ${execution_time}ms) ${RESET}"
            printf "${GREEN}${received_answer} ${CHECK_SYMBOL} ${RESET}\n"
        else
            printf "${PURPLE}${title} "
            printf "${GREY}(executed in ${execution_time}ms) ${RESET}"
            printf "${RED}${received_answer} ${CROSS_SYMBOL} ${RESET}\n"
            printf "Expected: $expected_answer, Got $received_answer\n"
            exit 1
        fi
    fi
}

run_part1() {
    echo "part 1"
}

run_part2() {
    echo "part 2"
}

run_solved() {
    full_title=$(jq -r ".fullTitle" "$json_file")

    input_file=$(jq -r ".inputFile" "$json_file")
    part1_title=$(jq -r ".part1.part" "$json_file")
    part1_output_file=$(jq -r ".part1.outputFile" "$json_file")

    part2_title=$(jq -r ".part2.part" "$json_file")
    part2_output_file=$(jq -r ".part2.outputFile" "$json_file")

    echo "$language(solved): $full_title"
    run "part1" "$part1_title" $input_file $part1_output_file
    run "part2" "$part2_title" $input_file $part2_output_file
}

main
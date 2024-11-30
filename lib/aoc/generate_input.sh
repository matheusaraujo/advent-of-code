#/bin/bash

aoc_generate_input() {
    if ! validate_year_day; then
        return 1
    elif [ -z "$part" ]; then
        echo -e "${RED}[ERROR] Part must be defined (part1 or part2).${NC}"
        return 1
    fi

    letter=$(ls $year/day$day/data/input.$part.*.txt 2>/dev/null | wc -l | awk '{printf "%c", 97 + $1}')

    echo "input(Ctrl+D to finish):"
    input=$(cat)

    mkdir -p $year/day$day/data
    echo "$input" > $year/day$day/data/input.$part.$letter.txt

    echo -e "\noutput:"
    read output

    echo "$output" > $year/day$day/data/output.$part.$letter.txt

}
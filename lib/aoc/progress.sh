#!/bin/bash

generate_progress_bar() {
    local solved_days=$1
    local total_days=25
    local filled=$((solved_days))
    local empty=$((total_days - solved_days))
    local progress_bar=""

    for ((i=0; i<filled; i++)); do
        progress_bar+="█"
    done

    for ((i=0; i<empty; i++)); do
        progress_bar+="-"
    done

    echo "$progress_bar"
}

aoc_progress() {
    emojis=("🎄" "🎅" "🎁" "❄️" "💻" "👨‍💻" "👩‍💻" "🧑‍💻" "🎉" "🧑‍🎄")

    README_FILE="README.md"

    new_content="<!-- progress-begin -->\n
| YEAR          | PROGRESS                      | COMPLETED (Out of 25) |
|---------------|-------------------------------|-----------------------|"

    for y in {2015..2024}; do
        solved_days=0
        
        for d in $(seq -f "%02g" 1 25); do
            if [ -d "$y/day$d" ] && [ -f "$y/day$d/README.md" ]; then
                solved_days=$((solved_days + 1))
            fi
        done

        emoji=${emojis[$RANDOM % ${#emojis[@]}]}
        progress=$(generate_progress_bar $solved_days)
        new_content+=$"\n| $emoji $y | $progress | $solved_days ($((solved_days * 100 / 25))%) |"
    done

    new_content+=$"\n<!-- progress-end -->"

    sed -i -e '/<!-- progress-begin -->/,/<!-- progress-end -->/d' "$README_FILE"
    echo -e "$new_content" >> "$README_FILE"

    print_success "progress updated! \033[32m✔\033[0m"

}
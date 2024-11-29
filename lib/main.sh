#!/bin/bash

# Color definitions
GREEN="\033[0;32m"
NC="\033[0m"
RED="\033[0;31m"

# Constants
YEARS=$(seq -w 2015 2035)
DAYS=$(seq -w 1 25)
COMMIG_MSG_SCRIPT=".githooks/commit-msg.sh"
GIT_HOOKS_DIR=".git/hooks"
COMMIT_MSG_HOOK_NAME="commit-msg"

# Utility function to validate year, day, and language
validate_year_day() {
    if [ -z "$year" ]; then
        echo -e "${RED}[ERROR] Year must be defined.${NC}"
        return 1
    elif [ -z "$day" ]; then
        echo -e "${RED}[ERROR] Day must be defined.${NC}"
        return 1
    fi
    return 0
}

validate_year_day_lang() {
    if [ -z "$year" ]; then
        echo -e "${RED}[ERROR] Year must be defined.${NC}"
        return 1
    elif [ -z "$day" ]; then
        echo -e "${RED}[ERROR] Day must be defined.${NC}"
        return 1
    elif [ -z "$lang" ]; then
        echo -e "${RED}[ERROR] Language must be defined.${NC}"
        return 1
    elif [[ "$lang" != "perl" && "$lang" != "python" ]]; then
        echo -e "${RED}[ERROR] Language must be either 'perl' or 'python'.${NC}"
        return 1
    fi
    return 0
}

# Help function: Display usage and commands
help() {
    echo -e "${GREEN}Usage:${NC} aoc <command> [options]"
    echo -e "\n${GREEN}Commands:${NC}"
    echo -e "  help                              Show help for each command."
    echo -e "  create <year> <day> <language>    Create a new challenge for the given year, day, and language."
    echo -e "  run <year> <day>                  Run the solution for the given year and day."
    echo -e "  commit <year> <day>               Commit the solution for the given year and day."
    echo -e "\n${GREEN}Examples:${NC}"
    echo -e "  aoc help"
    echo -e "    Show this help message."
    echo -e "  aoc create 2001 1 perl"
    echo -e "    Create a new challenge for 2001, Day 1, using Perl."
    echo -e "  aoc run 2001 1"
    echo -e "    Run the solution for 2001, Day 1."
    echo -e "  aoc commit 2001 1"
    echo -e "    Commit the solution for 2001, Day 1."
    echo -e "\n${GREEN}Starting:${NC}"
    echo -e "  Supported languages: perl, python"
    echo -e "\n${GREEN}Available Commands:${NC}"
    grep -E '^# COMMAND: ' "$0" | sed 's/# COMMAND: //' | while read -r cmd desc; do
        printf "  ${GREEN}%s${NC} %s\n" "$cmd" "$desc"
    done
}

# Parse arguments and set year, day, lang, part
parse_args() {
    while [[ $# -gt 0 ]]; do
        # If the argument is a number between 2015 and 2024, it's the $year
        if [[ $1 =~ ^[2][0][1-9][5-9]$ || $1 =~ ^[2][0][2][0-4]$ ]]; then
            year="$1"
        
        # If the argument is a number between 1 and 25 (1-9 as two digits, 10-25 as is), it's the $day
        elif [[ $1 =~ ^[0-9]{1,2}$ && $1 -ge 1 && $1 -le 25 ]]; then
            # If day is between 1 and 9, add leading zero
            if [[ $1 -ge 1 && $1 -le 9 ]]; then
                day=$(printf "%02d" $1)
            else
                day="$1"
            fi
        
        # Check if the argument is part1 or part2
        elif [[ $1 == "part1" || $1 == "part2" ]]; then
            part="$1"
        
        # Check if the argument is python or perl
        elif [[ $1 == "python" || $1 == "perl" ]]; then
            lang="$1"
        
        else
            echo "Unknown option: $1"
            exit 1
        fi
        shift
    done
}

# COMMAND: configure-hooks: Configure git hooks
configure_hooks() {
    echo "Installing Git hooks..."
    if [ ! -f "$COMMIG_MSG_SCRIPT" ]; then
        echo -e "${RED}[ERROR] Commit-msg script not found.${NC}"
        exit 1
    fi
    cp "$COMMIG_MSG_SCRIPT" "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    chmod +x "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    echo -e "${GREEN}Git hooks installed successfully.${NC}"
    [ ! -f ".session.cookie" ] && touch "session.cookie"
}

# COMMAND: create: Create a new solution for the given year, day, and lang
create() {
    if ! validate_year_day_lang; then
        return 1
    fi
    lib/create.sh "$year" "$day" "$lang"
}

# COMMAND: run: Execute the solution for given year and day
run() {
    if ! validate_year_day_lang; then
        return 1
    elif [ ! -d "$year/day$day" ]; then
        echo -e "${RED}[ERROR] Directory does not exist for $year, day $day.${NC}"
        return 1
    fi
    lib/run.sh "$year" "$day" "$part"
}

# COMMAND: run-all: Execute all solutions for all years and days
run_all() {
    for year in $YEARS; do
        for day in $DAYS; do
            if [ -d "$year/day$day" ]; then
                echo "----------------------------------------------------------------------"
                echo -e "${GREEN}Running $year day $day...${NC}"
                run "$year" "$day" || {
                    echo -e "${RED}[ERROR] Test failed for $year day $day.${NC}"
                    exit 1
                }
            fi
        done
    done
}

# COMMAND: lint: Run linters for given year and day
lint() {
    if ! validate_year_day; then
        return 1
    fi
    lib/lint.sh "$year" "$day"
}

# COMMAND: analysis: Run static code analysis for given year and day
analysis() {
    if ! validate_year_day; then
        return 1
    fi
    lib/analysis.sh "$year" "$day"
}

# COMMAND: analysis-all: Run static code analysis for all solutions
analysis_all() {
    for year in $YEARS; do
        for day in $DAYS; do
            if [ -d "$year/day$day" ]; then
                echo "----------------------------------------------------------------------"
                echo -e "${GREEN}Running analysis for $year day $day...${NC}"
                analysis "$year" "$day" || {
                    echo -e "${RED}[ERROR] Analysis failed for $year day $day.${NC}"
                    exit 1
                }
            fi
        done
    done
}

# COMMAND: commit: Validate and commit for given year and day
commit() {
    if ! validate_year_day; then
        return 1
    fi
    run
    lint
    analysis
    readme
    progress
    lib/commit.sh "$year" "$day"
}

# COMMAND: generate-input: Generate input for given year, day, and part
generate_input() {
    if ! validate_year_day; then
        return 1
    elif [ -z "$part" ]; then
        echo -e "${RED}[ERROR] Part must be defined (part1 or part2).${NC}"
        return 1
    fi
    lib/generate-input.sh "$year" "$day" "$part"
}

# Parse the command and run the corresponding function
if [ $# -eq 0 ]; then
    help
else
    cmd="$1"
    shift
    parse_args "$@"
    case "$cmd" in
        help) help ;;
        configure-hooks) configure_hooks ;;
        create) create ;;
        run) run ;;
        run-all) run_all ;;
        lint) lint ;;
        analysis) analysis ;;
        analysis-all) analysis_all ;;
        commit) commit ;;
        generate-input) generate_input ;;
        tree) lib/tree.sh ;;
        *) echo -e "${RED}[ERROR] Unknown command: $cmd${NC}"; help ;;
    esac
fi

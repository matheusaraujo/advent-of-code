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

source lib/parse_args.sh

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

# Watch function: Monitors changes in the directory and triggers the run function
watch() {
    local watch_dir="$year/day$day"
    
    echo -e "${GREEN}Running $watch_dir in watch mode...\nPress Ctrl+C to stop.${NC}"

    lib/run.sh "$year" "$day" "$part"

    inotifywait -m -r -e close_write,create,delete "$watch_dir" --exclude '\.pyc(\..*)?$' 2>/dev/null |
    while read -r directory events filename; do
        clear
        lib/run.sh "$year" "$day" "$part"
    done
}

# COMMAND: run: Execute the solution for given year and day
run() {
    if ! validate_year_day; then
        return 1
    elif [ ! -d "$year/day$day" ]; then
        echo -e "${RED}[ERROR] Directory does not exist for $year, day $day.${NC}"
        return 1
    fi
    if [ "$watch_mode" == "true" ]; then
        watch
    else
        lib/run.sh "$year" "$day" "$part"
    fi
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

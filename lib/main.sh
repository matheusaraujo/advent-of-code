#!/bin/bash

YEARS=$(seq -w 2015 2035)
DAYS=$(seq -w 1 25)

source lib/aoc/analysis.sh
source lib/aoc/commit.sh
source lib/aoc/configure_hooks.sh
source lib/aoc/create.sh
source lib/aoc/format.sh
source lib/aoc/generate_input.sh
source lib/aoc/help.sh
source lib/aoc/langs.sh
source lib/aoc/parse_args.sh
source lib/aoc/progress.sh
source lib/aoc/puzzle_text.sh
source lib/aoc/run.sh
source lib/aoc/utils.sh
source lib/aoc/validate_args.sh

# COMMAND: help: Show help message
help() {
    aoc_help
}

# COMMAND: setup: Configure git hooks
setup() {
    aoc_configure_hooks
}

# COMMAND: create: Create a new solution for the given year, day, and lang
create() {
    aoc_create
}

# COMMAND: run: Execute the solution for given year and day
run() {
    aoc_run
}

# COMMAND: generate-input: Generate sample input for given year, day, and part
generate_input() {
    aoc_generate_input
}

# COMMAND: run-all: Execute all solutions for all years and days
run_all() {
    for year in $YEARS; do
        for day in $DAYS; do
            if [ -d "$year/day$day" ]; then
                echo "----------------------------------------------------------------------"
                echo -e "${GREEN}Running $year day $day...${NC}"
                run || {
                    echo -e "${RED}[ERROR] Test failed for $year day $day.${NC}"
                    exit 1
                }
            fi
        done
    done
}

# COMMAND: format: Run formaters for given year and day
format() {
    aoc_format
}

# COMMAND: analysis: Run static code analysis for given year and day
analysis() {
    aoc_analysis
}

# COMMAND: analysis-all: Run static code analysis for all solutions
analysis_all() {
    for year in $YEARS; do
        for day in $DAYS; do
            if [ -d "$year/day$day" ]; then
                echo "----------------------------------------------------------------------"
                echo -e "${GREEN}Running analysis for $year day $day...${NC}"
                analysis || {
                    echo -e "${RED}[ERROR] Analysis failed for $year day $day.${NC}"
                    exit 1
                }
            fi
        done
    done
}

# COMMAND: puzzle-text: Fetch puzzle text for given year and day
puzzle_text() {
    aoc_puzzle_text
}

# COMMAND: progress: Update progress in README
progress() {
    aoc_progress
}

# COMMAND: commit: Validate and commit for given year and day
commit() {
    if ! validate_year_day; then
        return 1
    fi
    run
    format
    analysis
    puzzle_text
    progress
    aoc_commit
}

# Parse the command and run the corresponding function
main() {
    if [ $# -eq 0 ]; then
        help
    else
        cmd="$1"
        shift
        [ "$cmd" == "create" ] && rm -rf .aoc-env
        parse_args "$@"
        case "$cmd" in
            help) help ;;
            setup) setup ;;
            create) create ;;
            run) run ;;
            run-all) run_all ;;
            format) format ;;
            analysis) analysis ;;
            analysis-all) analysis_all ;;
            commit) commit ;;
            generate-input) generate_input ;;
            tree) lib/tree.sh ;;
            puzzle-text) puzzle_text ;;
            progress) progress ;;
            *) print_error "${RED}[ERROR] Unknown command: $cmd${NC}"; help ;;
        esac
    fi
}

main "$@"
#!/bin/bash

source lib/aoc/configure_hooks.sh
source lib/aoc/consts.sh
source lib/aoc/create.sh
source lib/aoc/help.sh
source lib/aoc/lint.sh
source lib/aoc/parse_args.sh
source lib/aoc/run.sh
source lib/aoc/utils.sh
source lib/aoc/validate_args.sh

# COMMAND: help: Show help message
help() {
    aoc_help
}

# COMMAND: configure-hooks: Configure git hooks
configure_hooks() {
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

# COMMAND: lint: Run linters for given year and day
lint() {
    aoc_lint
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

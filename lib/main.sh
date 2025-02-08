#!/bin/bash

YEARS=$(seq -w 2015 2035)
DAYS=$(seq -w 1 25)

source lib/aoc/check.sh
source lib/aoc/clean.sh
source lib/aoc/commit.sh
source lib/aoc/configure_hooks.sh
source lib/aoc/create.sh
source lib/aoc/format.sh
source lib/aoc/generate_input.sh
source lib/aoc/help.sh
source lib/aoc/langs.sh
source lib/aoc/langs_stats.sh
source lib/aoc/parse_args.sh
source lib/aoc/progress.sh
source lib/aoc/extract_answers.sh
source lib/aoc/run.sh
source lib/aoc/utils.sh
source lib/aoc/validate_args.sh
source lib/aoc/version.sh

# COMMAND: help: Show help message
help() {
    aoc_help
}

# COMMAND: configure_hooks: Configure git hooks
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

# COMMAND: run-year: Execute all solutions for given year
run_year() {
    validate_year
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
}

# COMMAND: format: Format for given year and day
format() {
    aoc_format
}

# COMMAND: check: Run checks for given year and day
check() {
    aoc_check
}

# COMMAND: version: Show versions of all tools
version() {
    aoc_version
}

# COMMAND: check-all: Run validations for all solutions
check_all() {
    for year in $YEARS; do
        for day in $DAYS; do
            if [ -d "$year/day$day" ]; then
                echo "----------------------------------------------------------------------"
                echo -e "${GREEN}Running validation for $year day $day...${NC}"
                check || {
                    echo -e "${RED}[ERROR] Validation failed for $year day $day.${NC}"
                    exit 1
                }
            fi
        done
    done
}

# COMMAND: check-year: Run validations for all solutions in given year
check_year() {
    validate_year
    for day in $DAYS; do
        if [ -d "$year/day$day" ]; then
            echo "----------------------------------------------------------------------"
            echo -e "${GREEN}Running validation for $year day $day...${NC}"
            check || {
                echo -e "${RED}[ERROR] Validation failed for $year day $day.${NC}"
                exit 1
            }
        fi
    done
}

# COMMAND: extract-answers: Fetch puzzle text for given year and day
extract_answers() {
    aoc_puzzle_text
}

# COMMAND: progress: Update progress in README
progress() {
    aoc_progress
}

# COMMAND: lang-stats: Update the language stats session in README
langs_stats() {
    aoc_lang_stats
}

# COMMAND: commit: Validate and commit for given year and day
commit() {
    if ! validate_year_day; then
        return 1
    fi
    format
    check
    run
    extract_answers
    progress
    langs_stats
    aoc_commit
}

# COMMAND: clean: Clean temporary files
clean() {
    aoc_clean
}

# Parse the command and run the corresponding function
main() {
    if [ $# -eq 0 ]; then
        help
    else
        cmd="$1"
        shift
        if [ "$cmd" == "create" ]; then
            infer_year_day
        fi
        parse_args "$@"
        case "$cmd" in
            help) help ;;
            configure_hooks) configure_hooks ;;
            create) create ;;
            run) run ;;
            run-all) run_all ;;
            run-year) run_year ;;
            format) format ;;
            check) check ;;
            check-all) check_all ;;
            check-year) check_year ;;
            commit) commit ;;
            generate-input) generate_input ;;
            tree) lib/tree.sh ;;
            extract-answers) extract_answers ;;
            progress) progress ;;
            lang-stats) langs_stats ;;
            version) version ;;
            clean) clean ;;
            *) print_error "${RED}[ERROR] Unknown command: $cmd${NC}"; help ;;
        esac
    fi
}

main "$@"

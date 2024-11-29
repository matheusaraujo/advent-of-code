#!/bin/bash

GREEN="\033[0;32m"
NC="\033[0m"
RED="\033[0;31m"

YEARS=$(seq -w 2015 2035)
DAYS=$(seq -w 1 25)

COMMIG_MSG_SCRIPT=".githooks/commit-msg.sh"
GIT_HOOKS_DIR=".git/hooks"
COMMIT_MSG_HOOK_NAME="commit-msg"

# Helper function to display help
help() {
    echo -e "${GREEN}help${NC}: Show help for each command."
    grep -E '^# COMMAND: ' "$0" | sed 's/# COMMAND: //' | while read -r cmd desc; do
        printf "${GREEN}%s${NC}: %s\n" "$cmd" "$desc"
    done
}

parse_args() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            year)
                year="$2"
                shift 2
                ;;
            day)
                day="$2"
                shift 2
                ;;
            lang)
                lang="$2"
                shift 2
                ;;
            part)
                part="$2"
                shift 2
                ;;
            test)
                test="$2"
                shift 2
                ;;
            *)
                echo "Unknown option: $1"
                exit 1
                ;;
        esac
    done
}

# COMMAND: configure-hooks: Configure git hooks
configure_hooks() {
    echo "Installing Git hooks..."
    if [ ! -f "$COMMIG_MSG_SCRIPT" ]; then
        echo "Error: Pre-commit script not found."
        exit 1
    fi
    cp "$COMMIG_MSG_SCRIPT" "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    chmod +x "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    echo -e "${GREEN}Git hooks installed successfully.${NC}"
    [ ! -f ".session.cookie" ] && touch "session.cookie"
}

# COMMAND: create: Create a new solution for given [year], [day], and [lang]
create() {
    if [ -z "$year" ]; then
        echo "[year] must be defined"
    elif [ -z "$day" ]; then
        echo "[day] must be defined"
    elif [ -z "$lang" ]; then
        echo "[lang] must be defined"
    elif [[ "$lang" != "perl" && "$lang" != "python" ]]; then
        echo "[lang] must be either 'perl' or 'python'"
    else
        lib/create.sh "$year" "$day" "$lang"
    fi
}

# COMMAND: run: Execute the solution for given [year] and [day]
run() {
    if [ -z "$year" ]; then
        echo "[year] must be defined"
    elif [ -z "$day" ]; then
        echo "[day] must be defined"
    elif [ ! -d "$year/day$day" ]; then
        echo "Directory does not exist"
    else
        lib/run.sh "$year" "$day" "$part" "$test"
    fi
}

# COMMAND: run-all: Execute all solutions
run_all() {
    for year in $YEARS; do
        for day in $DAYS; do
            if [ -d "$year/day$day" ]; then
                echo "----------------------------------------------------------------------"
                echo -e "${GREEN}Running $year day $day ...${NC}"
                run year="$year" day="$day" || {
                    echo -e "${RED}Test failed for $year day $day${NC}"
                    exit 1
                }
            fi
        done
    done
}

# COMMAND: lint: Run linters for given [year] and [day]
lint() {
    if [ -z "$year" ]; then
        echo "[year] must be defined"
    elif [ -z "$day" ]; then
        echo "[day] must be defined"
    elif [ ! -d "$year/day$day" ]; then
        echo "Directory does not exist"
    else
        lib/lint.sh "$year" "$day"
    fi
}

# COMMAND: analysis: Run static code analysis for given [year] and [day]
analysis() {
    if [ -z "$year" ]; then
        echo "[year] must be defined"
    elif [ -z "$day" ]; then
        echo "[day] must be defined"
    elif [ ! -d "$year/day$day" ]; then
        echo "Directory does not exist"
    else
        lib/analysis.sh "$year" "$day"
    fi
}

# COMMAND: analysis-all: Run static code analysis for all solutions
analysis_all() {
    for year in $YEARS; do
        for day in $DAYS; do
            if [ -d "$year/day$day" ]; then
                echo "----------------------------------------------------------------------"
                echo -e "${GREEN}Running analysis for $year day $day ...${NC}"
                analysis year="$year" day="$day" || {
                    echo -e "${RED}Analysis failed for $year day $day${NC}"
                    exit 1
                }
            fi
        done
    done
}

# COMMAND: readme: Generate README.md for given [year] and [day]
readme() {
    if [ -z "$year" ]; then
        echo "[year] must be defined"
    elif [ -z "$day" ]; then
        echo "[day] must be defined"
    elif [ ! -d "$year/day$day" ]; then
        echo "Directory does not exist"
    else
        lib/readme.sh "$year" "$day"
    fi
}

# COMMAND: progress: Display progress
progress() {
    lib/progress.sh
}

# COMMAND: commit: Validate and prepare commit for given [year] and [day]
commit() {
    if [ -z "$year" ]; then
        echo "[year] must be defined"
    elif [ -z "$day" ]; then
        echo "[day] must be defined"
    elif [ ! -d "$year/day$day" ]; then
        echo "Directory does not exist"
    else
        run
        lint
        analysis
        readme
        progress
        lib/commit.sh "$year" "$day"
    fi
}

# COMMAND: generate-input: Generate input for given [year], [day], and [part]
generate_input() {
    if [ -z "$year" ]; then
        echo "[year] must be defined"
    elif [ -z "$day" ]; then
        echo "[day] must be defined"
    elif [ -z "$part" ]; then
        echo "[part] must be defined as part1 or part2"
    else
        lib/generate-input.sh "$year" "$day" "$part"
    fi
}

tree() {
    lib/tree.sh
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
        readme) readme ;;
        progress) progress ;;
        commit) commit ;;
        generate-input) generate_input ;;
        tree) tree ;;
        *) echo "Unknown command: $cmd"; help ;;
    esac
fi

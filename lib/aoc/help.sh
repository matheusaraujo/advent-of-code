#!/bin/bash

aoc_help() {
    echo -e "${GREEN}Usage:${NC} aoc <command> [options]"
    echo -e "\n${GREEN}Commands:${NC}"
    echo -e "  help                              Show help message."
    echo -e "  create <year> <day> <language>    Create a new challenge for the given year, day, and language."
    echo -e "  run <year> <day> [--watch]        Run the solution for the given year and day. Use '--watch' to enable watch mode."
    echo -e "  commit <year> <day>               Commit the solution for the given year and day."
    echo -e "\n${GREEN}Examples:${NC}"
    echo -e "  aoc help"
    echo -e "    Show this help message."
    echo -e "  aoc create 2001 1 perl"
    echo -e "    Create a new challenge for 2001, Day 1, using Perl."
    echo -e "  aoc run 2001 1"
    echo -e "    Run the solution for 2001, Day 1."
    echo -e "  aoc run 2001 1 --watch"
    echo -e "    Run the solution for 2001, Day 1 in watch mode."
    echo -e "  aoc commit 2001 1"
    echo -e "    Commit the solution for 2001, Day 1."
    echo -e "\n${GREEN}Starting:${NC}"
    echo -e "  Supported languages: perl, python"
    echo -e "\n${GREEN}All available commands:${NC}"
    grep -E '^# COMMAND: ' "$0" | sed 's/# COMMAND: //' | while read -r cmd desc; do
        printf "  ${GREEN}%s${NC} %s\n" "$cmd" "$desc"
    done
}
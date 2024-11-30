#!/bin/bash

validate_year_day() {
    if [ -z "$year" ]; then
        print_error "${RED}[ERROR] Year must be defined.${NC}"
        return 1
    elif [ -z "$day" ]; then
        print_error "${RED}[ERROR] Day must be defined.${NC}"
        return 1
    fi
    return 0
}

validate_year_day_lang() {
    if [ -z "$year" ]; then
        print_error "${RED}[ERROR] Year must be defined.${NC}"
        return 1
    elif [ -z "$day" ]; then
        print_error "${RED}[ERROR] Day must be defined.${NC}"
        return 1
    elif [ -z "$lang" ]; then
        print_error "${RED}[ERROR] Language must be defined.${NC}"
        return 1
    elif [[ "$lang" != "perl" && "$lang" != "python" ]]; then
        print_error "${RED}[ERROR] Language must be either 'perl' or 'python'.${NC}"
        return 1
    fi
    return 0
}
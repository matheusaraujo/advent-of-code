#!/bin/bash

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
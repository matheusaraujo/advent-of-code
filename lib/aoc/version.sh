#!/bin/bash

aoc_version() {
    echo "aoc@v0.0.1"
    for lang in "${available_languages[@]}"; do
        if [ -f "lib/$lang/version.sh" ]; then
            lib/$lang/version.sh
        fi
    done
}


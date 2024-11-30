#!/bin/bash

languages=("python" "perl")

declare -A lang_extensions
lang_extensions=(
    ["perl"]="pl"
    ["python"]="py"
)

print_success() {
    local message=$1
    echo -e "$message"
}

print_error() {
    local message=$1
    echo -e "$message"
}
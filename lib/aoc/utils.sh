#!/bin/bash

# Color definitions
GREEN="\033[0;32m"
NC="\033[0m"
RED="\033[0;31m"

print_success() {
    local message=$1
    echo -e "$message"
}

print_error() {
    local message=$1
    echo -e "$message"
}
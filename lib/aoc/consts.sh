#!/bin/bash

# Color definitions
GREEN="\033[0;32m"
NC="\033[0m"
RED="\033[0;31m"

# Constants
YEARS=$(seq -w 2015 2035)
DAYS=$(seq -w 1 25)
COMMIT_MSG_SCRIPT=".githooks/commit-msg.sh"
GIT_HOOKS_DIR=".git/hooks"
COMMIT_MSG_HOOK_NAME="commit-msg"

# Languages
available_languages=(python perl)

declare -A language_extensions
language_extensions=(
    ["perl"]="pl"
    ["python"]="py"
)

declare -A language_aliases
language_aliases=(
    ["py"]="python"
    ["python"]="python"
    ["pl"]="perl"
    ["perl"]="perl"
)
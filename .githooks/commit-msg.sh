#!/bin/bash

check_conventional_commit() {
    COMMIT_MSG=$(grep -E '^(feat|fix|docs|style|refactor|perf|test|chore|ci)(\([a-zA-Z0-9-]+\))?: .{1,}' "$1")
    if [ -z "$COMMIT_MSG" ]; then
        echo "Error: Commit message does not follow conventional commit format."
        echo "Please use a message in the format: type(scope): description"
        exit 1
    fi
}


commit_msg_file="$1"
check_conventional_commit "$commit_msg_file"

exit 0
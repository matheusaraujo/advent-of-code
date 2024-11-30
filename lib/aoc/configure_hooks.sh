#!/bin/bash

aoc_configure_hooks() {
    echo "Installing Git hooks..."
    if [ ! -f "$COMMIG_MSG_SCRIPT" ]; then
        echo -e "${RED}[ERROR] Commit-msg script not found.${NC}"
        exit 1
    fi
    cp "$COMMIG_MSG_SCRIPT" "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    chmod +x "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    echo -e "${GREEN}Git hooks installed successfully.${NC}"
    [ ! -f ".session.cookie" ] && touch "session.cookie"
}
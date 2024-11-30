#!/bin/bash

aoc_configure_hooks() {
    print_success "Installing Git hooks..."
    if [ ! -f "$COMMIT_MSG_SCRIPT" ]; then
        print_error "${RED}[ERROR] Commit-msg script not found.${NC}"
        exit 1
    fi
    cp "$COMMIT_MSG_SCRIPT" "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    chmod +x "$GIT_HOOKS_DIR/$COMMIT_MSG_HOOK_NAME"
    print_success "${GREEN}Git hooks installed successfully.${NC}"
    [ ! -f ".session.cookie" ] && touch "session.cookie"
}
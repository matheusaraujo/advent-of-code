int part1(const char* puzzle_input) {
    int open_count = 0;
    int close_count = 0;
    int i = 0;

    while (puzzle_input[i] != '\0') {
        if (puzzle_input[i] == '(') {
            open_count++;
        } else if (puzzle_input[i] == ')') {
            close_count++;
        }
        i++;
    }

    return open_count - close_count;
}
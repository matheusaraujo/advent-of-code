int part2(const char* puzzle_input) {
    int floor = 0;
    for (int i = 0; puzzle_input[i] != '\0'; i++) {
        floor += puzzle_input[i] == '(' ? 1 : -1;
        if (floor == -1)
            return i + 1;
    }
    return 0;
}
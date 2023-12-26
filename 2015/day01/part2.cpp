#include <iostream>
#include <cstring>

using std::string;

int part2(const string& puzzle_input) {
    int floor = 0;

    for (int i = 0; i < puzzle_input.length(); i++) {
        if (puzzle_input[i] == '(') {
            floor = floor + 1;
        } else if (puzzle_input[i] == ')') {
            floor = floor - 1;
        }

        if (floor == -1) {
            return i + 1;
        }
    }

    return 0;
}

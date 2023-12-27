#include <iostream>
#include <cstring>

using std::string;

int part1(const string& puzzle_input) {
    int open_count = 0;
    int close_count = 0;

    for (char c : puzzle_input) {
        if (c == '(') {
            open_count++;
        } else if (c == ')') {
            close_count++;
        }
    }

    return open_count - close_count;
}
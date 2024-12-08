#include "aoc_helpers.h"

char *part2(char **puzzle_input) {
  int floor = 0;
  for (int i = 0; puzzle_input[0][i] != '\0'; i++) {
    floor += puzzle_input[0][i] == '(' ? 1 : -1;
    if (floor == -1) {
      return aoc_int_to_str(i + 1);
    }
  }
  return aoc_int_to_str(0);
}

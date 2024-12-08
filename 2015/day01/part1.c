#include "aoc_helpers.h"

char *part1(char **puzzle_input) {
  int count = 0;

  for (int i = 0; puzzle_input[0][i] != '\0'; i++) {
    count += puzzle_input[0][i] == '(' ? 1 : -1;
  }

  return aoc_int_to_str(count);
}

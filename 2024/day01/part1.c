#include <stdlib.h>

#include "aoc_helpers.h"
#include "helpers.h"

char *part1(char **puzzle_input, int size) {
  int result = 0;
  int left[size + 1], right[size + 1];

  parse_and_sort(puzzle_input, size, left, right);

  for (int i = 0; i < size; i++) {
    result += abs(left[i] - right[i]);
  }

  return aoc_int_to_str(result);
}
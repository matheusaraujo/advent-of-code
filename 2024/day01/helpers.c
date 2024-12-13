#include <stdlib.h>

#include "aoc_helpers.h"

void parse_and_sort(char **puzzle_input, int size, int *left, int *right) {
  for (int i = 0; i < size; i++) {
    int num1 = 0, num2 = 0;
    aoc_scanf(puzzle_input[i], "%d %d", &num1, &num2);
    left[i] = num1;
    right[i] = num2;
  }

  qsort(left, size, sizeof(int), aoc_cmp_asc);
  qsort(right, size, sizeof(int), aoc_cmp_asc);
}

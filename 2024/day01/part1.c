#include <stdio.h>
#include <stdlib.h>

#include "helpers.h"

char *part1(char **puzzle_input, int size) {
  int result = 0;
  int left[size + 1], right[size + 1];

  for (int i = 0; i < size; i++) {
    int num1, num2;
    sscanf(puzzle_input[i], "%d %d", &num1, &num2);
    left[i] = num1, right[i] = num2;
  }

  qsort(left, size, sizeof(int), cmp_asc);
  qsort(right, size, sizeof(int), cmp_asc);

  for (int i = 0; i < size; i++)
    result += abs(left[i] - right[i]);

  return intToString(result);
}
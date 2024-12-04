#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100000

#include "helpers.h"

char *part2(const char **puzzle_input, int size) {
  int result = 0;
  int left[size], right[size];
  int count[MAX_SIZE];

  aoc_memset(count, 0, sizeof(count));

  for (int i = 0; i < size; i++) {
    int num1 = 0, num2 = 0;
    aoc_scanf(puzzle_input[i], "%d %d", &num1, &num2);
    left[i] = num1, right[i] = num2;
  }

  for (int i = 0; i < size; i++) {
    count[right[i]]++;
  }

  for (int i = 0; i < size; i++) {
    result += left[i] * count[left[i]];
  }

  return aoc_int_to_str(result);
}
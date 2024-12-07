#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100000

#include "aoc_helpers.h"
#include "helpers.h"

char *part2(char **puzzle_input, int size) {
  int result = 0;
  int left[size], right[size];
  int count[MAX_SIZE];

  aoc_memset(count, 0, sizeof(count));

  parse_and_sort(puzzle_input, size, left, right);

  for (int i = 0; i < size; i++) {
    count[right[i]]++;
  }

  for (int i = 0; i < size; i++) {
    result += left[i] * count[left[i]];
  }

  return aoc_int_to_str(result);
}
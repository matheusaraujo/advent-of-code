#include <stdio.h>
#include "helpers.h"

char *part1(const char *puzzle_input) {
  int count = 0;

  for (int i = 0; puzzle_input[i] != '\0'; i++)
    count += puzzle_input[i] == '(' ? 1 : -1;

  return intToString(count);
}
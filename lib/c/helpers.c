#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *aoc_int_to_str(int num) {
  char *result = (char *)malloc(20 * sizeof(char));
  if (result == NULL)
    return NULL;
  sprintf(result, "%d", num);
  return result;
}

void aoc_scanf(const char *input, const char *format, ...) {
  va_list args;
  va_start(args, format);

  int result = vsscanf(input, format, args);

  va_end(args);

  if (result < 0) {
    fprintf(stderr, "Error parsing input: '%s'\n", input);
  } else if (result != 2) {

    fprintf(stderr, "Expected 2 values, but got %d values from input: '%s'\n",
            result, input);
  }
}

void aoc_memset(void *ptr, int value, size_t num) {
  if (ptr == NULL) {
    fprintf(stderr, "Error: NULL pointer passed to aoc_memset\n");
    return;
  }

  memset(ptr, value, num);
}

int aoc_cmp_asc(const void *a, const void *b) {
  return (*(int *)a - *(int *)b);
}
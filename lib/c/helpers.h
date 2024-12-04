#ifndef WORKSPACES_ADVENT_OF_CODE_LIB_C_HELPERS_H
#define WORKSPACES_ADVENT_OF_CODE_LIB_C_HELPERS_H

char* aoc_int_to_str(int num);
int aoc_cmp_asc(const void *a, const void *b);
void aoc_scanf(const char *input, const char *format, ...);
void aoc_memset(void *ptr, int value, size_t num);

#endif /* WORKSPACES_ADVENT_OF_CODE_LIB_C_HELPERS_H */
#include <stdio.h>
#include <stdlib.h>

char* intToString(int num) {
    char* result = (char*)malloc(20 * sizeof(char));
    if (result == NULL) return NULL;
    sprintf(result, "%d", num);
    return result;
}
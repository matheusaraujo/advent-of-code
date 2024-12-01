#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function prototypes for part1 and part2
extern int part1(char** puzzle_input);
extern int part2(char** puzzle_input);

int main(int argc, char* argv[]) {
    // if (argc != 4) {
    //     fprintf(stderr, "Usage: %s <year> <day> <part>\n", argv[0]);
    //     return 1;
    // }

    // Parse command-line arguments
    char* year = argv[1];
    char* day = argv[2];
    char* part = argv[3];

    // Determine which function to call
    int (*func)(char**) = NULL;
    if (strcmp(part, "part1") == 0) {
        func = part1;
    } else if (strcmp(part, "part2") == 0) {
        func = part2;
    } else {
        fprintf(stderr, "Invalid part: %s\n", part);
        return 1;
    }

    // Read input dynamically
    char** input_lines = NULL; // Pointer to an array of strings
    size_t input_count = 0;
    size_t capacity = 10; // Initial capacity

    input_lines = malloc(capacity * sizeof(char*));
    if (input_lines == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    char* buffer = NULL;
    size_t buffer_size = 0; // This will be dynamically adjusted by getline
    ssize_t line_length;

    while ((line_length = getline(&buffer, &buffer_size, stdin)) != -1) {
        // Remove newline character
        if (buffer[line_length - 1] == '\n') {
            buffer[line_length - 1] = '\0';
        }

        // Resize input_lines array if needed
        if (input_count >= capacity) {
            capacity *= 2; // Double the capacity
            char** temp = realloc(input_lines, capacity * sizeof(char*));
            if (temp == NULL) {
                fprintf(stderr, "Memory allocation failed\n");
                free(buffer);
                for (size_t i = 0; i < input_count; i++) {
                    free(input_lines[i]);
                }
                free(input_lines);
                return 1;
            }
            input_lines = temp;
        }

        // Store the line in input_lines
        input_lines[input_count] = strdup(buffer);
        if (input_lines[input_count] == NULL) {
            fprintf(stderr, "Memory allocation failed\n");
            free(buffer);
            for (size_t i = 0; i < input_count; i++) {
                free(input_lines[i]);
            }
            free(input_lines);
            return 1;
        }

        input_count++;
    }

    free(buffer); // Free buffer allocated by getline

    // Call the selected function
    int result = func(input_lines);
    printf("%d\n", result);

    // Free memory
    for (size_t i = 0; i < input_count; i++) {
        free(input_lines[i]);
    }
    free(input_lines);

    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "part1.h"
#include "part2.h"

char* read_file(const char* file_path) {
    FILE* file = fopen(file_path, "r");
    if (file == NULL) {
        printf("File not found.\n");
        return NULL;
    }

    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    rewind(file);

    char* content = (char*)malloc(file_size + 1);
    if (content == NULL) {
        fclose(file);
        return NULL;
    }

    size_t read_size = fread(content, sizeof(char), file_size, file);
    if (read_size != file_size) {
        fclose(file);
        free(content);
        return NULL;
    }

    content[file_size] = '\0';
    fclose(file);
    return content;
}

char* extract_value(const char* content, const char* start_tag, const char* end_tag) {
    const char* start_ptr = strstr(content, start_tag);
    if (start_ptr == NULL) {
        return "";
    }

    start_ptr += strlen(start_tag);
    const char* end_ptr = strstr(start_ptr, end_tag);
    if (end_ptr == NULL) {
        return "";
    }

    size_t value_length = end_ptr - start_ptr;
    char* extracted_value = (char*)malloc(value_length + 1);
    if (extracted_value == NULL) {
        return NULL;
    }

    strncpy(extracted_value, start_ptr, value_length);
    extracted_value[value_length] = '\0';
    return extracted_value;
}

char* extract_nested_value(const char* content, const char* parent_tag, const char* start_tag, const char* end_tag) {
    const char* start_index_ptr = strstr(content, parent_tag);
    if (start_index_ptr == NULL) {
        return "";
    }

    start_index_ptr = strstr(start_index_ptr, start_tag);
    if (start_index_ptr == NULL) {
        return "";
    }

    start_index_ptr += strlen(start_tag);
    const char* end_index_ptr = strstr(start_index_ptr, end_tag);
    if (end_index_ptr == NULL) {
        return "";
    }

    size_t value_length = end_index_ptr - start_index_ptr;
    char* extracted_value = (char*)malloc(value_length + 1);
    if (extracted_value == NULL) {
        return NULL;
    }

    strncpy(extracted_value, start_index_ptr, value_length);
    extracted_value[value_length] = '\0';
    return extracted_value;
}

char** extract_properties(const char* file_content) {
    if (file_content == NULL || strlen(file_content) == 0) {
        printf("File content is empty.\n");
        return NULL;
    }

    char* title = extract_value(file_content, "\"title\": \"", "\"");
    char* year = extract_value(file_content, "\"year\": \"", "\"");
    char* day = extract_value(file_content, "\"day\": \"", "\"");
    char* input_file = extract_value(file_content, "\"inputFile\": \"", "\"");
    char* part1_output_file = extract_nested_value(file_content, "\"part1\":", "\"outputFile\": \"", "\"");
    char* part2_output_file = extract_nested_value(file_content, "\"part2\":", "\"outputFile\": \"", "\"");

    char** properties = (char**)malloc(6 * sizeof(char*));
    properties[0] = title;
    properties[1] = year;
    properties[2] = day;
    properties[3] = input_file;
    properties[4] = part1_output_file;
    properties[5] = part2_output_file;

    return properties;
}

int main(int argc, char* argv[]) {
    char file_path[100];
    snprintf(file_path, sizeof(file_path), "data/%s-%s.json", argv[1], argv[2]);

    char* file_content = read_file(file_path);
    if (file_content == NULL) {
        return 1;
    }

    char** extracted_properties = extract_properties(file_content);
    if (extracted_properties == NULL) {
        free(file_content);
        return 1;
    }

    char* title = extracted_properties[0];
    char* year = extracted_properties[1];
    char* day = extracted_properties[2];
    char* input_file = extracted_properties[3];
    char* part1_output_file = extracted_properties[4];
    char* part2_output_file = extracted_properties[5];

    printf("c: Running AoC %s Day %s - %s\n", year, day, title);

    char* input = read_file(input_file);

    int expected_result_part1 = atoi(read_file(part1_output_file));
    clock_t start_time1 = clock();
    int answer1 = part1(input);
    clock_t end_time1 = clock();
    double execution_time1 = ((double)(end_time1 - start_time1)) / CLOCKS_PER_SEC * 1000;

    if (answer1 != expected_result_part1) {
        printf("Part 1 Failed\n");
        return 1;
    }

    printf("\033[35mPart 1: \033[32m%d\033[3;90m (executed in %.2fms) \033[0m\n", answer1, execution_time1);

    int expected_result_part2 = atoi(read_file(part2_output_file));
    clock_t start_time2 = clock();
    int answer2 = part2(input);
    clock_t end_time2 = clock();
    double execution_time2 = ((double)(end_time2 - start_time2)) / CLOCKS_PER_SEC * 1000;

    if (answer2 != expected_result_part2) {
        printf("Part 2 Failed\n");
        return 1;
    }

    printf("\033[35mPart 2: \033[32m%d\033[3;90m (executed in %.2fms) \033[0m\n", answer2, execution_time2);

    free(title);
    free(year);
    free(day);
    free(input_file);
    free(part1_output_file);
    free(part2_output_file);
    free(extracted_properties);
    free(file_content);
    free(input);

    return 0;
}

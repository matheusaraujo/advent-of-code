struct Puzzle {
    int initialized;
    char* title;
    char* year;
    char* day;
    char* inputFile;
    char* part1_outputFile;
    char* part2_outputFile;
};

char* read_file(const char* file_path);
char* extract_value(const char* content, const char* start_tag, const char* end_tag);
char* extract_nested_value(const char* content, const char* parent_tag, const char* start_tag, const char* end_tag);
struct Puzzle read_puzzle(const char* file_content);

char* read_file(const char* file_path) {
    FILE* file = fopen(file_path, "r");
    if (file == NULL) {
        printf("File not found - %s.\n", file_path);
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

struct Puzzle read_puzzle(const char* file_path) {

    struct Puzzle puzzle;
    puzzle.initialized = 0;

    char* file_content = read_file(file_path);

    if (file_content == NULL || strlen(file_content) == 0) {
        printf("File content is empty.\n");
        return puzzle;
    }

    puzzle.initialized = 1;
    puzzle.title = extract_value(file_content, "\"title\": \"", "\"");
    puzzle.year = extract_value(file_content, "\"year\": \"", "\"");
    puzzle.day = extract_value(file_content, "\"day\": \"", "\"");
    puzzle.inputFile = extract_value(file_content, "\"inputFile\": \"", "\"");
    puzzle.part1_outputFile = extract_nested_value(file_content, "\"part1\":", "\"outputFile\": \"", "\"");
    puzzle.part2_outputFile = extract_nested_value(file_content, "\"part2\":", "\"outputFile\": \"", "\"");

    free(file_content);

    return puzzle;
}
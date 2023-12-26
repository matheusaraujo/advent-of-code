#include <iostream>
#include <fstream>
#include <cstring>
#include <ctime>
#include "part1.h"
#include "part2.h"

using std::cout;
using std::endl;
using std::ifstream;
using std::ios;
using std::setprecision;
using std::streampos;
using std::string;
using std::stoi;
using std::vector;

string read_file(const string& file_path) {
    ifstream file(file_path, ios::binary | ios::ate);
    if (!file.is_open()) {
        cout << "File not found." << endl;
        return "";
    }

    streampos file_size = file.tellg();
    file.seekg(0, ios::beg);

    string content;
    content.resize(file_size);
    file.read(&content[0], file_size);

    file.close();
    return content;
}

string extract_value(const string& content, const string& start_tag, const string& end_tag) {
    size_t start_pos = content.find(start_tag);
    if (start_pos == string::npos) {
        return "";
    }

    start_pos += start_tag.length();
    size_t end_pos = content.find(end_tag, start_pos);
    if (end_pos == string::npos) {
        return "";
    }

    return content.substr(start_pos, end_pos - start_pos);
}

string extract_nested_value(const string& content, const string& parent_tag, const string& start_tag, const string& end_tag) {
    size_t start_index_pos = content.find(parent_tag);
    if (start_index_pos == string::npos) {
        return "";
    }

    start_index_pos = content.find(start_tag, start_index_pos);
    if (start_index_pos == string::npos) {
        return "";
    }

    start_index_pos += start_tag.length();
    size_t end_index_pos = content.find(end_tag, start_index_pos);
    if (end_index_pos == string::npos) {
        return "";
    }

    return content.substr(start_index_pos, end_index_pos - start_index_pos);
}

vector<string> extract_properties(const string& file_content) {
    if (file_content.empty()) {
        cout << "File content is empty." << endl;
        return {};
    }

    vector<string> properties(6);

    properties[0] = extract_value(file_content, R"("title": ")", R"(")");
    properties[1] = extract_value(file_content, R"("year": ")", R"(")");
    properties[2] = extract_value(file_content, R"("day": ")", R"(")");
    properties[3] = extract_value(file_content, R"("inputFile": ")", R"(")");
    properties[4] = extract_nested_value(file_content, R"("part1":)", R"("outputFile": ")", R"(")");
    properties[5] = extract_nested_value(file_content, R"("part2":)", R"("outputFile": ")", R"(")");

    return properties;
}

int main(int argc, char* argv[]) {

    string file_path = "data/" + string(argv[1]) + "-" + string(argv[2]) + ".json";

    string file_content = read_file(file_path);
    if (file_content.empty()) {
        return 1;
    }

    vector<string> extracted_properties = extract_properties(file_content);
    if (extracted_properties.size() != 6) {
        return 1;
    }

    string title = extracted_properties[0];
    string year = extracted_properties[1];
    string day = extracted_properties[2];
    string input_file = extracted_properties[3];
    string part1_output_file = extracted_properties[4];
    string part2_output_file = extracted_properties[5];

    cout << "cpp: Running AoC " << year << " Day " << day << " - " << title << endl;

    string input = read_file(input_file);

    int expected_result_part1 = stoi(read_file(part1_output_file));
    clock_t start_time1 = clock();
    int answer1 = part1(input);
    clock_t end_time1 = clock();
    double execution_time1 = ((double)(end_time1 - start_time1)) / CLOCKS_PER_SEC * 1000;

    if (answer1 != expected_result_part1) {
        cout << "Part 1 Failed" << endl;
        return 1;
    }

    cout << "\033[35mPart 1: \033[32m" << answer1
        << "\033[3;90m (executed in " << setprecision(2)
        <<  execution_time1 << "ms) \033[0m\n";

    int expected_result_part2 = stoi(read_file(part2_output_file));
    clock_t start_time2 = clock();
    int answer2 = part2(input);
    clock_t end_time2 = clock();
    double execution_time2 = ((double)(end_time2 - start_time2)) / CLOCKS_PER_SEC * 1000;

    if (answer2 != expected_result_part2) {
        cout << "Part 2 Failed" << endl;
        return 1;
    }

    cout << "\033[35mPart 2: \033[32m" << answer2
        << "\033[3;90m (executed in " << setprecision(2)
        <<  execution_time2 << "ms) \033[0m\n";

    return 0;
}

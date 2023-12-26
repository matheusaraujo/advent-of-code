import json
import sys


def read_plain_txt_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def write_plain_txt_file(file_name, content):
    with open(f"{file_name}", "w", encoding="utf-8") as file:
        file.write(content)


def read_json_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = json.load(file)
    return content


def write_json_file(file_name, content):
    with open(f"{file_name}", "w", encoding="utf-8") as json_file:
        json.dump(convert_keys_to_camel_case(content), json_file, indent=4)


def number_to_string(n):
    n += 1
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = ""
    while n > 0:
        remainder = (n - 1) % 26
        result = alphabet[remainder] + result
        n = (n - 1) // 26

    return result


def format_time(execution_time):
    if execution_time >= 1:
        return f"{execution_time:.2f}s"
    return f"{(execution_time * 1000):.2f}ms"


def get_puzzle():
    return int(sys.argv[1]), int(sys.argv[2])


def import_puzzle_code(year, day):
    sys.path.append(f"{year}/day{day:02d}")


def to_camel_case(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def convert_keys_to_camel_case(obj):
    if isinstance(obj, dict):
        camel_case_dict = {}
        for key, value in obj.items():
            camel_case_key = to_camel_case(key)
            camel_case_dict[camel_case_key] = convert_keys_to_camel_case(value)
        return camel_case_dict

    if isinstance(obj, list):
        return [convert_keys_to_camel_case(item) for item in obj]

    return obj

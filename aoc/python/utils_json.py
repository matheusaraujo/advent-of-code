import json
from dataclasses import asdict
from models import Puzzle, Part


def read_puzzle_from_json(file_name) -> Puzzle:
    with open(file_name, "r", encoding="utf-8") as file:
        content = json.load(file)
    return Puzzle(
        title=content["title"],
        year=content["year"],
        day=content["day"],
        input_file=content["inputFile"],
        part1=Part(
            solved=content["part1"]["solved"],
            output_file=content["part1"]["outputFile"],
            examples=[],
        ),
        part2=Part(
            solved=content["part2"]["solved"],
            output_file=content["part2"]["outputFile"],
            examples=[],
        ),
    )


def write_puzzle_to_json(file_name: str, puzzle: Puzzle):
    with open(f"{file_name}", "w", encoding="utf-8") as json_file:
        json.dump(__convert_keys_to_camel_case(asdict(puzzle)), json_file, indent=4)


def __convert_keys_to_camel_case(obj):
    def __to_camel_case(snake_str):
        components = snake_str.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    if isinstance(obj, dict):
        camel_case_dict = {}
        for key, value in obj.items():
            camel_case_key = __to_camel_case(key)
            camel_case_dict[camel_case_key] = __convert_keys_to_camel_case(value)
        return camel_case_dict

    if isinstance(obj, list):
        return [__convert_keys_to_camel_case(item) for item in obj]

    return obj

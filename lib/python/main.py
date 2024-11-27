import sys
import time
from pathlib import Path
from typing import List, Optional

solution_path = f"./{sys.argv[1]}/day{sys.argv[2]}"
sys.path.append(solution_path)
from part1 import part1

if Path(f"{solution_path}/part2.py").exists():
    from part2 import part2
else:
    part2 = None


def main():
    year, day, part_name, input_file, *output_file = sys.argv[1:]
    output_file = output_file[0] if output_file else None

    input_data = read_file(input_file)
    expected_output = read_file(output_file, single_line=True) if output_file else None

    execute_part(
        part_name,
        input_file,
        part1 if part_name == "part1" else part2,
        input_data,
        expected_output,
    )


def read_file(
    file_path: Optional[str], single_line: bool = False
) -> Optional[List[str]]:
    if not file_path:
        return None
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines[0].strip() if single_line else [line.strip() for line in lines]


def execute_part(
    part_name: str,
    input_file: str,
    part_function,
    input_data: List[str],
    expected_output: Optional[str],
):
    input_label = get_input_file_label(input_file)

    start_time = time.perf_counter()
    result = part_function(input_data)
    elapsed_time = (time.perf_counter() - start_time) * 1000  # ms

    (result_check, result_symbol) = get_result_symbol(result, expected_output)
    print(
        format_result_message(
            part_name, input_label, result, elapsed_time, result_symbol
        )
    )

    if not result_check:
        exit(1)


def get_input_file_label(input_file: str) -> str:
    file_name = Path(input_file).name
    return "" if file_name == "input.txt" else f"({Path(input_file).stem})"


def get_result_symbol(result: str, expected_output: Optional[str]) -> str:
    if expected_output is None:
        return (True, "")

    return (
        str(result) == str(expected_output),
        (
            "\033[32m✔\033[0m"
            if str(result) == str(expected_output)
            else f"\033[91m ✘ {expected_output} \033[0m"
        ),
    )


def format_result_message(
    part_name: str,
    input_label: str,
    result: str,
    elapsed_time: float,
    result_symbol: str,
) -> str:
    return (
        f"\033[35m{part_name}{input_label}: \033[0m"
        f"\033[32m{result}\033[3;90m (executed in {elapsed_time:.4f}ms)"
        f"{result_symbol}\033[0m"
    )


if __name__ == "__main__":
    main()

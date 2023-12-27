import os


def read_plain_txt_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    return content


def write_plain_txt_file(file_name, content):
    directory = os.path.dirname(file_name)
    os.makedirs(directory, exist_ok=True)
    with open(f"{file_name}", "w", encoding="utf-8") as file:
        file.write(content)

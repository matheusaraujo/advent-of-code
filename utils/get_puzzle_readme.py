import re
import sys

import markdownify
import requests
from get_puzzle_commons import get_current_repo_remote_url, get_session_cookie


def download_file(year, day):
    url = f"https://adventofcode.com/{year}/day/{str(int(day))}"
    headers = {"User-Agent": get_current_repo_remote_url()}
    cookies = {"session": get_session_cookie()}

    response = requests.get(url, headers=headers, cookies=cookies, timeout=10)

    html = response.text

    pattern = r"<main\b[^>]*>(.*?)</main>"
    match = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
    html = match.group(1).strip()

    md = markdownify.markdownify(html, heading_style="ATX", bullets="-+*")
    try:
        i1 = md.index("Both parts of this puzzle are complete!")
    except ValueError:
        print("this problem is not solved yet!")
        return

    md = md[0:i1]
    md = md.replace("Your puzzle answer was", "> Your puzzle answer was")

    destination = f"{year}/day{day}/README.md"
    with open(destination, "w", encoding="UTF8") as file:
        file.write(md)

    print(f"> readme file created successfully at {destination}")


if len(sys.argv) != 3:
    print("> invalid arguments")
else:
    download_file(sys.argv[1], sys.argv[2])

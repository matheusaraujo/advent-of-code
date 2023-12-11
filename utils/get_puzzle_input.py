import sys
import urllib.request

from get_puzzle_commons import get_current_repo_remote_url, get_session_cookie


def download_file(year, day):
    url = f"https://adventofcode.com/{year}/day/{str(int(day))}/input"
    headers = {"User-Agent": get_current_repo_remote_url()}
    cookies = {"session": get_session_cookie()}

    destination = f"{year}/day{day}/input.txt"
    opener = urllib.request.build_opener()
    opener.addheaders = list((key, value) for key, value in headers.items())
    opener.addheaders.append(
        ("Cookie", "; ".join([f"{key}={value}" for key, value in cookies.items()]))
    )
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(url, destination)
    print(f"> input file downloaded successfully to {destination}")


if len(sys.argv) != 3:
    print("> invalid arguments")
else:
    download_file(sys.argv[1], sys.argv[2])

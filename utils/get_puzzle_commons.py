import os
import subprocess


def get_session_cookie():
    if os.path.exists("session.cookie"):
        with open("session.cookie", encoding="utf-8") as f:
            line = f.read()
        return line

    if os.environ.get("AOC_SESSION_COOKIE"):
        return os.environ.get("AOC_SESSION_COOKIE")

    print("> session.cookie not found, input will not be downloaded!")
    os._exit(0)


def get_current_repo_remote_url():
    remote_url = (
        subprocess.check_output(["git", "config", "--get", "remote.origin.url"])
        .decode()
        .strip()
    )
    return remote_url

import os
import subprocess


def get_session_cookie():
    if not os.path.exists("session.cookie"):
        print("> session.cookie file not found, input will not be downloaded!")
        os._exit(0)

    with open("session.cookie", encoding="utf-8") as f:
        line = f.read()
    return line


def get_current_repo_remote_url():
    remote_url = (
        subprocess.check_output(["git", "config", "--get", "remote.origin.url"])
        .decode()
        .strip()
    )
    return remote_url

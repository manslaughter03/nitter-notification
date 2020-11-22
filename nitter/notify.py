"""

notify module
"""
import os
import subprocess
import pkg_resources


def send_notify(description: str, dunstify_bin: str = "/usr/bin/dunstify"):
    """

    send notify
    :param description:
    """
    if not os.path.isfile(dunstify_bin):
        raise Exception(f"Can't find dunstify bin in path {dunstify_bin}")
    icon_path = pkg_resources.resource_filename(__name__, "resources/twitter.png")
    cmd = [dunstify_bin,
           "-a",
           "nitter",
           description,
           "-i",
           icon_path]
    process = subprocess.Popen(cmd)
    process.communicate()

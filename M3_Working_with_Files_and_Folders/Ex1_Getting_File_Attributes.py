import os
from datetime import datetime

import frequently_used_directories as dir


def get_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime("%d %b %Y")


def get_file_attributes(folder):
    print("Modified:\tFile name:")
    with os.scandir(folder) as dir:
        for item in dir:
            if item.is_file():
                attrs = item.stat()
                print(f"{get_date(attrs.st_mtime)}\t{item.name}")


get_file_attributes(dir.home)

import os

import frequently_used_directories as dir


def list_dir(folder):
    for content in os.listdir(folder):
        print(content)


list_dir(dir.dev)

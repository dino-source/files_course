import os

import frequently_used_directories as dir


def ends_with(folder, search_criterion):
    for content in os.listdir(folder):
        if content.endswith(search_criterion):
            print(content)


def starts_with(folder, search_criterion):
    for content in os.listdir(folder):
        if content.startswith(search_criterion):
            print(content)


# ends_with(dir.home, ".mkv")
starts_with(dir.home, "Do")

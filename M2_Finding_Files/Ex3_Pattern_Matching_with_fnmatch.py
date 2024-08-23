import fnmatch
import os

import frequently_used_directories as dir


def match(folder, search_criterion):
    for content in os.listdir(folder):
        if fnmatch.fnmatch(content, search_criterion):
            print(content)


# match(dir.home, '*.mkv')
# match(dir.medical_tests, "*Creatinin*.pdf")
# match(dir.medical_tests, "*22_12_20*.pdf")
match(dir.medical_tests, "*.pdf")

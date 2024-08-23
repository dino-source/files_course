import fnmatch
import os

import frequently_used_directories as dir


def match(folder, search_criterion):
    for content in os.listdir(folder):
        if fnmatch.fnmatch(content, search_criterion):
            print(content)


# match(dir.medical_tests, "*_12*.*")
# match(dir.medical_tests, "*_12_*.*")
match(dir.medical_tests, "*22_*_*.*")

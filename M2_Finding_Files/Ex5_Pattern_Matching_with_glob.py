from pathlib import Path

import frequently_used_directories as dir


def glob_match(folder, search_criterion):
    path = Path(folder)
    for content in path.glob(search_criterion):
        print(content)


# glob_match(dir.medical_tests, "*12*.p*")
glob_match(dir.medical_tests, "*Analysis*")

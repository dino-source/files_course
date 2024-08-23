import os

import frequently_used_directories as dir


def traverse(folder):
    for folder_path, dirs, files in os.walk(folder):
        print(f"Folder: {folder_path}")
        for file in files:
            print(f"\tFile: {file}")


traverse(dir.Documents)

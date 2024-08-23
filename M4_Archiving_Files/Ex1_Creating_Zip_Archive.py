# import time
import os
import zipfile

import frequently_used_directories as dir


def remove(f):
    if os.path.exists(f) and os.path.isfile(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error: {f}: {e.strerror}")
    else:
        print(f"Error: {f} is not a file")


to_zip = [
    f"{dir.home}/asdf.txt",
    f"{dir.notes}/new_idea.txt",
    f"{dir.dev}/hello/main.cpp",
    f"{dir.home}/2023-01-18 17-40-02.mkv",
]


def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)


my_zip = "./files.zip"
create_zip(my_zip, to_zip, "w")
# time.sleep(3)
# remove(my_zip)

import os

import frequently_used_directories as dir


def remove_file(f):
    if os.path.exists(f) and os.path.isfile(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error: {f}: {e.strerror}")
    else:
        print(f"Error: {f} is not a file")


# file = f"{dir.notes}/unique_new_file.txt"
# if os.path.exists(file):
#     remove_file(file)
# else:
#     with open(file, "x+") as f:
#         f.write("Surprise, motherfucker!")
#         f.seek(0)
#         print(f.read())
#         f.close()

# remove_file(file)

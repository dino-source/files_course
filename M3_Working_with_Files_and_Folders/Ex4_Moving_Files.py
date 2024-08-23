import shutil

import frequently_used_directories as dir


def move(src, dst):
    shutil.move(src, dst)


# file = f"{dir.Downloads}/IMG_7533.JPG"
# to_directory = dir.Pictures
# move(file, to_directory)

# folder = f"{dir.home}/edu"
# to_directory = f"{dir.notes}/xyz"
# move(folder, to_directory)

# folder = f"{dir.notes}/xyz"
# to_directory = f"{dir.home}/edu"
# move(folder, to_directory)

import shutil

import frequently_used_directories as dir


def copy_file(src, dst):
    shutil.copy(src, dst)


def copy_tree(src, dst):
    shutil.copytree(src, dst)


src = f"{dir.Documents}/dox/"
dst = f"{dir.Documents}/notes/"

# copy_file(src, dst)
copy_tree(src, dst + "new_folder/")

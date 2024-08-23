import os
from pathlib import Path

import frequently_used_directories as dir


def rename_file_1(src, dst):
    os.rename(src, dst)


def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)


f1 = f"{dir.edu}/tmux.shortcuts.md"
f2 = f"{dir.edu}/tmux_key_bindings.md"
rename_file_1(f1, f2)

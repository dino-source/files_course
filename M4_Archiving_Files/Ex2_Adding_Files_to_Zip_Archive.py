import zipfile

import frequently_used_directories as dir

file1 = f"{dir.home}/tmux-client-59938.log"
file2 = f"{dir.Music}/Hein Braat/Gayatri_Mantra.mp3"
to_add = [file1, file2]


def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            lst = archive.namelist()
            if f not in lst:
                archive.write(f)
            else:
                print(f"File exists in zip: {f}")


add_to_zip("./files.zip", to_add, "a")

import zipfile


def read_zip(zipf):
    with zipfile.ZipFile(zipf, "r") as archive:
        name_list = archive.namelist()
        for name in name_list:
            zfinf = archive.getinfo(name)
            fs = zfinf.file_size
            cs = zfinf.compress_size
            print(f"{name} => {fs} bytes, {cs} bytes compressed")


read_zip("./files.zip")

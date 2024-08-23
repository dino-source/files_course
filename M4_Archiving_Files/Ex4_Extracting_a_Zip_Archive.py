import zipfile


def extract_file(zip_file, file, path):
    with zipfile.ZipFile(zip_file, "r") as archive:
        archive.extract(file, path=path)


def extract_all(zip_file, path):
    with zipfile.ZipFile(zip_file, "r") as archive:
        archive.extractall(path=path)


# extract_file("./files.zip", "home/dino/asdf.txt", "extracted")
extract_all("./files.zip", "extracted")

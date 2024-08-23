def read_text_from_file(file):
    with open(file) as f:
        print(f.read())
    f.close()


def read_text_from_file_line_by_line(file):
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            print(line, sep="")
            line = f.readline()
    f.close()


def write_text_to_file(file, string):
    with open(file) as f:
        with open(file, "w", encoding="utf-8") as f:
            f.write(string)


def append_text_to_file(file, string):
    with open(file, "a", encoding="utf-8") as f:
        f.write("\n")
        f.write(string)
    f.close()


# read_text_from_file("/home/dino/asdf.txt")
# read_text_from_file_line_by_line("/home/dino/dev/py/oop_course/README.md")

# msg = "\nDo What Thou Wilt Shall Be The Whole Of The Law"
# write_text_to_file("/home/dino/asdf.txt", msg)
# read_text_from_file("/home/dino/asdf.txt")

append_text_to_file("/home/dino/asdf.txt", "Is there anybody out there?")
read_text_from_file("/home/dino/asdf.txt")

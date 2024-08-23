import csv
import os


def read_csv(file, delimiter):
    with open(file) as csv_file:
        counter = -1
        tab = "\t"
        header = f"{tab}|{tab}"
        rows = csv.reader(csv_file, delimiter=delimiter)
        for row in rows:
            if counter == -1:
                print(f"{header.join(row)}")
            else:
                msg_p1 = f"{row[0]}{tab}|{tab}{row[1]}{tab}"
                msg_p2 = f"|{tab}{row[2]}{tab}|{tab}{row[3]}"
                print(msg_p1 + msg_p2)
            counter += 1
        print(f"{counter} lines")


def write_csv(file, header, row):
    if not os.path.exists(file):
        with open(file, mode="w", newline="") as csv_file:
            qm = csv.QUOTE_MINIMAL
            csvf = csv_file
            writer = csv.writer(csvf, delimiter=",", quotechar='"', quoting=qm)
            writer.writerow(header)
            writer.writerow(row)
    else:
        with open(file, mode="a", newline="") as csv_file:
            qm = csv.QUOTE_MINIMAL
            csvf = csv_file
            writer = csv.writer(csvf, delimiter=",", quotechar='"', quoting=qm)
            writer.writerow(row)


# read_csv("./names.csv", ',')
file = "./employees.csv"
header = ["name", "surname", "age", "gender"]
write_csv(file, header, ["Juan", "Batista", "43", "male"])
write_csv(file, header, ["Bill", "Rassell", "23", "male"])
write_csv(file, header, ["Kira", "Nightly", "34", "female"])
write_csv(file, header, ["Mike", "Freeman", "45", "male"])

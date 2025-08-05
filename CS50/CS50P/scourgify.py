import csv
import sys

new = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row["name"].split(",")
            new.append([first.strip(), last.strip(), row["house"]])
except FileNotFoundError:
    sys.exit("File not found")
except IndexError:
    sys.exit("Please specify a file")
else:
    try:
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for list in new:
                writer.writerow({"first": list[0], "last": list[1], "house": list[2]})
    except IndexError:
        sys.exit("Please specify the new filename")

import sys


if len(sys.argv) != 2:
    sys.exit("Not enough parameters")

c = 0
if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a python File")

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.lstrip().startswith("#") == False:
                if line.strip() != "":
                    c += 1
except FileNotFoundError:
    sys.exit("Not a valid file")

else:
    print(c)

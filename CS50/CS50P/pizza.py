from tabulate import tabulate
import sys

list = []

try:
    with open(sys.argv[1]) as file:
        for item in file:
            pizza, cs, cl = item.strip().split(",")
            list.append([pizza, cs, cl])
except FileNotFoundError:
    sys.exit("File not found")
except IndexError:
    sys.exit("Please specify a file")
print(tabulate(list, headers = "firstrow", tablefmt = "grid"))

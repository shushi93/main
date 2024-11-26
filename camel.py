s = input("camelCase: ")
for c in s:
    if (c.upper() == c):
        print("_", c.lower(), sep = "", end = "")
    else:
        print(c, end = "")

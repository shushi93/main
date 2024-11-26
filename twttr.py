s = input("Hello ")
for c in s:
    #print(c)
    if (c.lower() != "a" and c.lower()  != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u"):
        print(c, end = "")
    else:
        continue

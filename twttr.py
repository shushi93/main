def main():
    s = input("Hello ")
    s = shorten(s)
    print(s)

def shorten(word):
    l = ""
    word = str(word)
    for c in word:
        if (c.lower() != "a" and c.lower()  != "e" and c.lower() != "i" and c.lower() != "o" and c.lower() != "u"):
            l += c
        else:
            continue
    return l

if __name__ == "__main__":
    main()

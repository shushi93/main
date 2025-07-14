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
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

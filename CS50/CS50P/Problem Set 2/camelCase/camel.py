s = input("camelCase: ")
for c in s:
    if (c.upper() == c):
        print("_", c.lower(), sep = "", end = "")
    else:
        print(c, end = "")
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

match x:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

def main():
    x = input("A customer comes in ")
    x = value(x)
    print(f"${x}")

def value(greeting):
    greeting = greeting.strip().lower()
    if (greeting.startswith("hello")):
        return 0
    elif (greeting.startswith("h")):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

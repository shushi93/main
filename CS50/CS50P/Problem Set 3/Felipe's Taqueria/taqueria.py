menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
cost = 0
while True:
    try:
        x = input("Item: ").title()
        cost += menu[x]
        print(f"Cost: ${cost:.2f}")
    except KeyError:
        pass
    except EOFError:
        break
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

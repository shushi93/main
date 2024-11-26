cost = 50
while (cost > 0):
    x = int(input("Insert coin: "))
    match x:
        case 5:
            cost -= 5
        case 10:
            cost -= 10
        case 25:
            cost -=25
    if (cost > 0):
        print("Amount Due:", cost)

print("Change Owed:", abs(cost))
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

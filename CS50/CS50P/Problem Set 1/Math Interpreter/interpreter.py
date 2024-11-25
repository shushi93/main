expression = input("What do you want to calculate? ")
x, y, z = expression.split(" ")
x = float(x)
z = float(z)
#print(y)
if (y == "+"):
    print(x + z)
elif(y == "-"):
    print(x - z)

elif (y == "*"):
    print (x * z)

else:
    print(x / z)
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

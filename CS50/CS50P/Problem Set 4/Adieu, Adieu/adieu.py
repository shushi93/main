import inflect
p = inflect.engine()
arr = []
while True:
    try:
        x = input("Name: ")
        arr.append(x)
    except EOFError:
        break
    except KeyboardInterrupt:
        break
result = p.join(arr)
print ("Adieu, adieu, to", result)
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

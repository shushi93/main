while True:
    try:
        tank = input("Fraction: ")
        x, y = tank.split("/")
        x = int(x)
        y = int(y)
        if (x/y > 1):
            continue
        elif (x/y >= .99):
            print("F")
            break
        elif (x/y <= .1):
            print("E")
            break
        else:
            print(round(x / y * 100), "%", sep="") # had to use chatgpt bcos i didnt know how to make x / y return a non-float value
            break
    except (ValueError, ZeroDivisionError):
        pass
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

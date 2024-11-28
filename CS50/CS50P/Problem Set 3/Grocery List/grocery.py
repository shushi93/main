items = {}
while True:
    try:
        x = input().upper()
        y = items.get(x, 0)
        y += 1
        items[x] = y
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    except KeyError:
        print("Item is not a string")
print()
for i in sorted(items.keys()):
    print(items[i], i)
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

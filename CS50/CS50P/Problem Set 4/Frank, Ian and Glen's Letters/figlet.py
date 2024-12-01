from pyfiglet import Figlet
import sys, random
figlet = Figlet()
arr = figlet.getFonts()
if len(sys.argv) == 3:
    if (sys.argv[1] != "-f" and sys.argv[1] != "--font"):
        sys.exit("Not enough parameters")
    else:
        print(sys.argv[2])
        if (sys.argv[2] in arr):
            x = input("Text: ").strip()
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(x))
        else:
            sys.exit("Not a valid font")
else:
    if len(sys.argv) == 2:
        sys.exit("Not enough parameters")
    r = random.choice(arr)
    x = input("Text: ").strip()
    figlet.setFont(font=r)
    print(figlet.renderText(x))
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

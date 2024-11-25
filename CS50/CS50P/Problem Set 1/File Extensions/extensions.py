x = input("File: ").strip().lower()

if (x.endswith(".jpg") or x.endswith(".jpeg")):
    print("image/jpeg")
elif x.endswith(".pdf"):
    print("application/pdf")
elif x.endswith(".gif"):
    print("image/gif")
elif x.endswith(".png"):
    print("image/png")
elif x.endswith(".txt"):
    print("text/plain")
elif x.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

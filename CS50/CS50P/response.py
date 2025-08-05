import validators

if validators.email(input("What is your email?")):
    print("Valid")
else:
    print("Invalid")

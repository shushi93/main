def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s) > 1 and len(s) < 7):
        if (64 < ord(s[0]) < 91 and 64 < ord(s[1]) < 91):
            if (not_number_at_mid(s)):
                if (not_invalid_char(s)):
                    if (num_0_letterless(s)):
                        return True
    return False

def not_number_at_mid(s):
    carry = False
    for i in s:
        if (carry == False and 47 < ord(i) < 57):
            carry = True
        elif (carry == True and 64 < ord(i) < 91):
            return False
    return True

def num_0_letterless(s):
    first = False
    for i in s:
        if (first == False and ord(i) == 48):
            return False
        if (47 < ord(i) < 57):
            break
    if (47 < ord(s[0]) < 57):
        return False
    return True
def not_invalid_char(s):
    for i in s:
        if (31 < ord(i) < 48):
            return False
    return True
if __name__ == "__main__":
    main()
#DO NOT COPY AND PASTE THIS CODE AND SUBMIT IT. THIS WOULD GO AGAINST THE ACADEMY'S POLICY ON ACADEMIC HONESTY. ONLY READ THEM IF YOU WANT TO CONFIRM YOUR CODE, OR YOU ARE EXTREMELY STUCK ON THE PROBLEM AND NEED A REFERENCE

def main():
    x = input("What time is it? ")
    h = convert(x)
    if (7 <= h <= 8):
        print("breakfast time")
    elif (12 <= h <= 13):
        print("lunch time")
    else:
        print("dinner time")

def convert(time):
   h, min =  time.split(":")
   min = int(min)
   h = float(h)
   h += min/60
   return h

if __name__ == "__main__":
    main()

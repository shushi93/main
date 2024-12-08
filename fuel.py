import sys


def main():
    tank = input("Fraction: ")
    tank = convert(tank)
    print(f"{gauge(tank)}")


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if (x/y >= 1):
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    percentage = float(percentage)
    if (percentage >= 99):
        return "F"
    elif (percentage <= 1):
        return "E"
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()

import random


def main():
    n = get_level()
    e = 0
    c = 0
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        print(f"{x} + {y} = ")
        while True:
            while True:
                try:
                    ans = int(input("Answer: "))
                    break
                except ValueError:
                    pass
            if (x + y != ans):
                e += 1
                print("EEE")
                if (e == 3):
                    print(f"{x} + {y} = {x + y}")
                    break
            else:
                c += 1
                break
    print("Score:", c)

def get_level():
    while True:
        n = input("Level: ")
        try:
            n = int(n)
            if (n < 1 or n > 3):
                raise ValueError
            return int(n)
        except ValueError:
            pass


def generate_integer(level):
    if (level == 1):
        g = random.randint(0, 9)
    elif (level == 2):
        g = random.randint(10, 99)
    else:
        g = random.randint(100, 999)
    return g


if __name__ == "__main__":
    main()

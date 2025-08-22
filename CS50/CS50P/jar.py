import re

class Jar:
    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError
        else:
            self._capacity = capacity
            self.cookies = 0
    def __str__(self):
        cookies = ""
        #if self.cookies <= 0:
            #print("deposit some cookies first!")
        #else:
        for i in range(self.cookies):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        n = int(n)
        if self.cookies + n > self.capacity:
            raise ValueError("too many cookies deposited. eat some!")
        else:
            self.cookies += n
            #print("well, i guess i'll save it for later")
            #print(f"+{self.cookies} added to jar")

    def withdraw(self, n):
        n = int(n)
        self.eat = n
        if self.cookies < n:
            raise ValueError("not enough cookies to eat from the jar")
        else:
            self.cookies -= n
            #print("i. need. my. cookies. nom nom nom")
            #print(f"{self.cookies} eaten")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

def main():
    jar = Jar()
    print("Don't know what to do? type 'help'!")
    while True:
        act = input("Action: ").strip()
        if act == "help":
            print("deposit [n] (adds n cookies to cookie jar) \n \
                  withdraw [n] (takes away n cookies from cookie jar) \n \
                  capacity (returns cookie jar's capacity) \n \
                  size (returns how many cookies in the cookie jar right now) \n \
                  cookie (run it by itself to see what it does) \n \
                  exit (exits the program)")
        elif act.startswith("deposit"):
            #try:
            n = re.search(r"^deposit (?P<num>\d+)$", act)
            jar.deposit(n.group("num"))
        elif act.startswith("withdraw"):
            #try:
            n = re.search(r"^withdraw (?P<num>\d+)$", act)
            jar.withdraw(n.group("num"))
        elif act.startswith("capacity"):
            print(jar.capacity)
        elif act.startswith("size"):
            print(jar.size)
        elif act.startswith("cookie"):
            print(str(jar))
        elif act == "exit":
            break

if __name__ == "__main__":
    main()

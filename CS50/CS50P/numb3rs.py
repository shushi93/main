import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.fullmatch(r"(0|[1-9]([0-9])?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])?\.(0|[1-9]([0-9])?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])?\.(0|[1-9]([0-9])?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])?\.(0|[1-9]([0-9])?|1[0-9][0-9]|2[0-4][0-9]|25[0-5])?", ip)
    #print(matches.group())
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

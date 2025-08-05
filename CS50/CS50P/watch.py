import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    findurl = re.search(r'<iframe.*?src="http(s)?://(www\.)?youtube\.com/embed/(?P<url>\w+)".*?></iframe>', s, re.IGNORECASE)
    if findurl:
        return f"https://youtu.be/{findurl.group("url")}"

if __name__ == "__main__":
    main()

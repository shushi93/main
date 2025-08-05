import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    ct = ""
    time = re.search(r"""(?P<num1>[1-9]|([1][0-2]))
                     (:(?P<min1>00|0[1-9]|[1-5][0-9]))? \s
                     (?P<time1>AM|PM) \s to \s
                     (?P<num2>[1-9]|([1][0-2]))
                     (:(?P<min2>00|0[1-9]|[1-5][0-9]))? \s
                     (?P<time2>AM|PM)""", s, re.IGNORECASE | re.VERBOSE)
    if time:
        if time.group("num1") and not time.group("num1") is None:
            h1 = int(time.group("num1"))
        else:
            raise ValueError

        if time.group("min1") is None:
            m1 = 00
        elif int(time.group("min2")) < 60:
            m1 = int(time.group("min1"))
        else:
            raise ValueError

        if time.group("num2") and not time.group("num2") is None:
            h2 = int(time.group("num2"))
        else:
            raise ValueError

        if time.group("min2") is None:
            m2 = 00
        elif int(time.group ("min2")) < 60:
            m2 = int(time.group("min2"))
        else:
            raise ValueError

        if time.group("time1") == "AM" or time.group("time1") == "PM":
            time1 = time.group("time1")
        else:
            raise ValueError

        if time.group("time2") == "AM" or time.group("time2") == "PM":
            time2 = time.group("time2")
        else:
            raise ValueError

        if time1 == "AM":
            if h1 < 12:
                ct += f"{h1:02}:{m1:02}"
            else:
                ct += f"00:{m1:02}"
        elif time1 == "PM":
            if h1 < 12:
                ct += f"{h1 + 12:02}:{m1:02}"
            else:
                ct += f"{h1:02}:{m1:02}"

        ct += " to "
        #print(f"time2 {time2}")
        if time2 == "AM":
            if h2 < 12:
                ct += f"{h2:02}:{m2:02}"
            else:
                ct += f"00:{m2}"
        elif time2 == "PM":
            if h2 < 12:
                ct += f"{h2 + 12:02}:{m2:02}"
            else:
                ct += f"{h2:02}:{m2:02}"

        return ct
    else:
        raise ValueError

if __name__ == "__main__":
    main()

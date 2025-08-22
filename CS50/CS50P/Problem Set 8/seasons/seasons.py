from datetime import datetime
from datetime import date
import sys
import inflect
p  = inflect.engine()


def age(bday):
    day = date.today()
    try:
        if bday[0].isdigit():
            birthday = date.fromisoformat(bday)
        else:
            birthday = datetime.strptime(bday, "%B %d, %Y").date()
        interval = day - birthday
        mins =  (interval.days) * 1440
        return p.number_to_words(mins).replace("and ", "").capitalize()
    except ValueError:
        sys.exit("Invalid date/format")


def main():
    print(age(input("When were you born?").strip()), "minutes")


if __name__ == "__main__":
    main()


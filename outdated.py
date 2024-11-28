dates = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        x = input("Date: ")
        try:
            m, d, y = x.split("/")
            d = int(d)
            m = int(m)
            y = y.strip()
            if (d > 31):
                raise ValueError()
            if (m > 12):
                raise ValueError()
        except:
            m, d, y = x.split()
            d = int(d[:-1])
            if (d > 31):
                raise ValueError()
            m = dates.index(m) + 1
            if(m > 12):
                raise ValueError()
            y = y.strip()
        print(f"{y}-{m:02}-{d:0>2}")
        break
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    except ValueError:
        pass

import requests
import sys
import json

try:
    x = float(sys.argv[1])
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json"
    )
    o = response.json()
    n = float(o["bpi"]["USD"]["rate_float"])
    print(f"${(n * x):,.4f}")

except ValueError:
    sys.exit("Value cannot be converted to float")
except IndexError:
    sys.exit("Not enough parameters")
except requests.RequestException:
    sys.exit("Something went wrong")

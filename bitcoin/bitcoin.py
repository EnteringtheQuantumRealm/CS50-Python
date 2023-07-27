# n = command-line argument the number of Bitcoins
# If n argument cannot be converted to a float, the program should exit via sys.exit with an error message
# Queries the API for the CoinDesk Bitcoin Price Index:
# https://api.coindesk.com/v1/bpi/currentprice.json, (returns a JSON object)
# Be sure to catch any exceptions (requests.RequestException, null, ValueError)
# ['bpi']['USD']['rate_float'] # print(json.dumps((response.json()), indent = 4, sort_keys = True))

import sys
import requests
import json

def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(btc_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    elif len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        pass

def btc_price(number):
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        amount = price * number
        return f"${amount:,.4f}"
    except requests.RequestException:
        return None

main()
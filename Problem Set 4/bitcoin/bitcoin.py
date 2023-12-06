import sys
import requests


def main():
    get_bitcoin_in_USD()


def get_bitcoin_in_USD():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        bitcoin_data = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json"
        ).json()
    except requests.RequestException:
        sys.exit("There's an error processing your request. Try again later.")
    bitcoin_rate = bitcoin_data["bpi"]["USD"]["rate_float"]
    amount_cost = bitcoin_rate * amount
    print(f"${amount_cost:,.4f}")


main()

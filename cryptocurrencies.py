from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {"start": "1", "limit": "5000", "convert": "USD"}
headers = {
    "Accepts": "application/json",
    "Accept-Encoding": "deflate, gzip",
    "X-CMC_PRO_API_KEY": "b5d11021-8bdc-4691-88d5-c623a92718f2"
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


my_dict = {}
for item in data["data"]:
    my_dict[item["name"].lower()] = item["quote"]["USD"]["price"]


def do_you_want_to_continue():
    while True:
        choice = input("Do you want to continue checking rates? Type yes or no: ")
        choice = choice.lower()
        if choice not in ("yes", "no"):
            print("Didn't get it. Please check your answer.")
            continue
        elif choice == "yes":
            return True
        else:
            print("Thanks, see you soon!")
            return False


while True:
    coin = input("Enter the full name of the currency: ")
    coin = coin.lower()
    if coin in my_dict:
        print(my_dict[coin])
        want_to_continue = do_you_want_to_continue()
        if not want_to_continue:
            break
    else:
        print("Didn't get it. Please check your answer.")
        continue


# TODO would you like to update your wallet?
# TODO enter your purchases
# TODO check what's in your wallet

import requests

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_59tzGHRfkd1TkgN0b49j3Ancf2YbakWJCMdM8PUr"

print("Fetching latest exchange rates...")
response = requests.get(BASE_URL + "v1/latest?apikey=" + API_KEY)
data = response.json()
rates_data = data["data"]

rates = {}
for code in rates_data:
    rates[code] = rates_data[code]

print("\nYou can convert between these currencies:")
for code in sorted(rates.keys()):
    print(code, end="  ")
print("\n")

amount_str = input("Enter the amount you want to convert: ")
try:
    amount = float(amount_str)
except:
    print("That isn’t a valid number. Goodbye.")
    exit()

src = input("Enter the source currency code: ").upper()
dst = input("Enter the target currency code: ").upper()


if src not in rates or dst not in rates:
    print("Unknown currency code. Please run again with codes from the list.")
    exit()


amount_in_usd = amount / rates[src]
result = amount_in_usd * rates[dst]

print()
print(amount, src, "=", round(result, 2), dst)

import requests


def user_input():
    data= []
    amount = int(input("Amount to convert: "))

    initial_currency = str(input("Initial Currency to convert from?: ")).upper()
    while len(initial_currency) != 3:
        initial_currency = str(input("Initial Currency to convert from?: ")).upper()

    final_currency = str(input("Final Currency to convert to?: ")).upper()
    while len(final_currency) != 3:
         final_currency = str(input("Final Currency to convert to?: ")).upper()

    data += amount, initial_currency, final_currency
    return data

def fetch_exchange_rate(data):
    base = data[1]
    quotes = data[2]
    url = f"https://api.frankfurter.dev/v2/rates"
    params = {
        "base": base,
        "quotes": quotes
    }
    try:
        res = requests.get(url=url, params=params)
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 422:
            print("422 Client Error: Unprocessable Entity")
        elif err.response.status_code == 404:
            print("404 Client Error: Not Found")
        else:
            raise
        #print(err)
        
    else:
        result = res.json()
        rate = [i["rate"] for i in result][0]
        
            
        return rate

def calculate_new_amount(exchange_rate, data):
    rate =  exchange_rate
    # if rate is not int:
    #     print("test")
    amount = data[0]
    new_amount = amount * rate
    return new_amount


def main():
    input_data = user_input()
    rate = fetch_exchange_rate(input_data)
    if rate is not None:
        new_amount = calculate_new_amount(rate, input_data)
        print(f"{input_data[0]} {input_data[1]} is {new_amount} {input_data[2]} with the exchange rate of {rate}.")
    else:
        print(f"Try Again!")
    

if __name__ == "__main__":
    main()

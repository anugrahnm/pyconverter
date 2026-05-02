from nt import error
import requests
import pytest

def user_input():
    data= []
    while True:
        try:
            amount = int(input("Amount to convert: "))
            if amount <= 0:
                print("Invalid Amount, Try Again!")
                continue
            break
        except ValueError:
            print("Invalid Amount, Try Again!")
            continue

    # while amount <= 0:
    #     amount = int(input("Invalid Amount, Try Again! Amount to convert: "))


     

    initial_currency = str(input("1 Initial Currency to convert from?: ")).upper()
    while len(initial_currency) != 3:
        try:
             initial_curr = int(initial_currency)

        except ValueError:
            break
        else:
        
            print("1 Only Alphabets Allowed! Try Again!")
            initial_currency = str(input("2 Initial Currency to convert from?: ")).upper()  
            continue
            
            # except ValueError:
            #     initial_currency = str(initial_currency)



    # while len(initial_currency) != 3:
        
    #     try:
    #         initial_currency = int(initial_currency)
    #     except ValueError:
    #         initial_currency = str(initial_currency)
            
    #     try:
    #         print("3 Only Alphabets Allowed! Try Again!")
    #         initial_currency = str(input("4 Initial Currency to convert from?: ")).upper()
    #     except ValueError: 
    #         initial_currency = str(initial_currency)

    final_currency = str(input("Final Currency to convert to?: ")).upper()
    while len(final_currency) != 3:
         final_currency = str(input("Invalid Currency, Try Again! Final Currency to convert to?: ")).upper()

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
    if rate is None or rate == 0 or rate < 0:
        return "invalid currency"
    else:
        amount = data[0]
        new_amount = amount * rate
        return new_amount


def main():
    input_data = user_input()
    rate = fetch_exchange_rate(input_data)

    new_amount = calculate_new_amount(rate, input_data)
    if new_amount == "invalid currency":
        print("Invalid Currency, Try Again!")
    else:   
        print(f"{input_data[0]} {input_data[1]} is {new_amount} {input_data[2]} with the exchange rate of {rate}.")
    

if __name__ == "__main__":
    main()


# def test_calculate_new_amount():
#     assert calculate_new_amount(1.28, [100, "USD" , "EUR"]) == 128
import requests


class CurrencyConverter():
    def __init__(self):
        self.amount = None
        self.initial_currency = None
        self.final_currency = None
        self.rate = None
        self.new_amount = None


    def get_input(self):
        while True:
            try:
                self.amount = int(input("Amount to convert: "))
                if self.amount <= 0:
                    print("Invalid Amount, Try Again!")
                    continue
                break
            except ValueError:
                print("Invalid Amount, Try Again!")
                continue
    
        while True:
            self.initial_currency = str(input("Initial Currency to convert from?: ")).upper()

            if self.initial_currency.isalpha():
                if len(self.initial_currency) != 3:
                    print("Invalid Currency, Try Again!")
                    continue
                else:
                    break
            else:
                print("Only Alphabets Allowed! Try Again!")
                continue
    
        while True:
            self.final_currency = str(input("Final Currency to convert to?: ")).upper()

            if self.final_currency.isalpha():
                if len(self.final_currency) != 3:
                    print("Invalid Currency, Try Again!")
                    continue
                else:
                    break
            else:
                print("Only Alphabets Allowed! Try Again!")
                continue

    def fetch_rates(self):
        base = self.initial_currency
        quotes = self.final_currency
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
        else:
            result = res.json()
            self.rate = [i["rate"] for i in result][0]

    def calculate(self):
        
        if self.rate is None or self.rate == 0 or self.rate < 0:
            self.new_amount = "invalid currency"
        else:
            self.new_amount = self.amount * self.rate
    
    def display(self):
        if self.new_amount == "invalid currency":
            print("Invalid Currency, Try Again!")
        else:   
            print(f"{self.amount} {self.initial_currency} is {self.new_amount} {self.final_currency} with the exchange rate of {self.rate}.")

def main():
    currency = CurrencyConverter()
    currency.get_input()
    currency.fetch_rates()
    currency.calculate()
    currency.display()

if __name__ == "__main__":
    main()
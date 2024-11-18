from api.upbit_api import UpbitAPI

class Trader:
    def __init__(self):
        self.api = UpbitAPI()

    def get_balance(self):
        accounts = self.api.get_accounts()
        print(f"accounts: {accounts}")
        # for account in accounts:
            # print(f"Currency: {account['currency']}, Balance: {account['balance']}")

    def get_market_price(self, market):
        ticker = self.api.get_ticker(market)
        return ticker[0]['trade_price'] if ticker else None

    def place_buy_order(self, market, amount):
        price = self.get_market_price(market)
        if price:
            volume = amount / price
            return self.api.place_order(market, "bid", volume, price, "limit")
        return None

    def place_sell_order(self, market, volume):
        price = self.get_market_price(market)
        if price:
            return self.api.place_order(market, "ask", volume, price, "limit")
        return None
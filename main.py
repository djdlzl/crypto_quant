import json
from trading.trader import Trader

def main():
    trader = Trader()
    
    # 계좌 잔고 조회
    trader.get_balance()
    
    # 비트코인 시장가 조회
    btc_price = trader.get_market_price("KRW-BTC")
    print(f"Current BTC price: {btc_price}")
    
    # 전체 종목 조회
    currency = trader.get_market_all()
    print(f"Tatal Curreny: {json.dumps(currency, indent=2, ensure_ascii=False)}")
    
    # # 10만원어치 비트코인 구매 주문
    # buy_order = trader.place_buy_order("KRW-BTC", 100000)
    # if buy_order:
    #     print("Buy order placed successfully")
    # else:
    #     print("Failed to place buy order")

if __name__ == "__main__":
    main()
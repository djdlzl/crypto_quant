from utils.auth import UpbitAuth

class UpbitAPI:
    def __init__(self):
        self.auth = UpbitAuth()

    def get_accounts(self):
        """계좌 조회"""
        endpoint = "/v1/accounts"
        return self.auth.request_get(endpoint)

    def get_market_all(self, is_details=False):
        """마켓 코드 조회"""
        endpoint = "/v1/market/all"
        params = {'isDetails': 'true' if is_details else 'false'}
        return self.auth.request_get(endpoint, params)

    def get_ticker(self, markets):
        """현재가 정보"""
        endpoint = "/v1/ticker"
        params = {"markets": markets}
        return self.auth.request_get(endpoint, params)

    def place_order(self, market, side, volume, price, ord_type):
        """주문하기"""
        endpoint = "/v1/orders"
        data = {
            "market": market,
            "side": side,
            "volume": volume,
            "price": price,
            "ord_type": ord_type
        }
        return self.auth.request_post(endpoint, data)
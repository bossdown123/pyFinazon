
class SIP:
    def __init__(self, outer):
        self._send_request = outer._send_request
    def trades(self, ticker, market=None, start_at=None, end_at=None, tape=None, page=0, page_size=10, order="DESC"):
        params = {
            'ticker': ticker,
            'market': market,
            'start_at': start_at,
            'end_at': end_at,
            'tape': tape,
            'page': page,
            'page_size': page_size,
            'order': order
        }
        return self._send_request("/sip/trades", params)
    def market_center(self):
        return self._send_request("/sip/market_center")

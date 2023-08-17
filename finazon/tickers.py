
class Tickers:
    def __init__(self, outer):
        self._send_request = outer._send_request
    def crypto(self, publisher, ticker=None, page=0, page_size=100):
        params = {
            'publisher': publisher,
            'ticker': ticker,
            'page': page,
            'page_size': page_size
        }
        return self._send_request("/tickers/crypto", params)
    def stocks(self, publisher, ticker=None, page=0, page_size=100):
        params = {
            'publisher': publisher,
            'ticker': ticker,
            'page': page,
            'page_size': page_size
        }
        return self._send_request("/tickers/stocks", params)
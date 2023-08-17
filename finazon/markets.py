
class Markets:
    def __init__(self, outer):
        self._send_request = outer._send_request
    def crypto(self, page=0, page_size=100):
        params = {
            'page': page,
            'page_size': page_size
        }
        return self._send_request("/markets/crypto", params)
    def stocks(self, country=None, name=None, code=None, page=0, page_size=100):
        params = {
            'country': country,
            'name': name,
            'code': code,
            'page': page,
            'page_size': page_size
        }
        return self._send_request("/markets/stocks", params)
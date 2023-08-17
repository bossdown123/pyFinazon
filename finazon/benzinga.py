
class Benzinga:
    def __init__(self, outer):
        self._send_request = outer._send_request
    def dividends_calendar(self, ticker, date=None, start_at=None, end_at=None, page=0, page_size=100, order="DESC"):
        params = {
            'ticker': ticker,
            'date': date,
            'start_at': start_at,
            'end_at': end_at,
            'page': page,
            'page_size': page_size,
            'order': order
        }
        return self._send_request("/benzinga/dividends_calendar", params)
    def earnings_calendar(self, ticker, date=None, start_at=None, end_at=None, page=0, page_size=100, order="DESC"):
        params = {
            'ticker': ticker,
            'date': date,
            'start_at': start_at,
            'end_at': end_at,
            'page': page,
            'page_size': page_size,
            'order': order
        }
        return self._send_request("/benzinga/earnings_calendar", params)
    def news(self, ticker, date=None, start_at=None, end_at=None, page=0, page_size=100, order="DESC"):
        params = {
            'ticker': ticker,
            'date': date,
            'start_at': start_at,
            'end_at': end_at,
            'page': page,
            'page_size': page_size,
            'order': order
        }
        return self._send_request("/benzinga/news", params)
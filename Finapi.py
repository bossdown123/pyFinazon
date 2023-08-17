
import requests
class Finazon:
    BASE_URL = "https://api.finazon.io/v1.0"
    
    def __init__(self, api_key):
        self.api_key = api_key
        
    def _send_request(self, endpoint, params={}):
        headers = {
            'accept': 'application/json',
            'Authorization': f"apikey {self.api_key}"
        }
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        return response
    
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

    def get_ticker_snapshot(self, publisher, ticker, market=None, country=None):
        params = {
            'publisher': publisher,
            'ticker': ticker,
            'market': market,
            'country': country
        }
        return self._send_request("/ticker/snapshot", params)

    def get_sec_archive(self, cik_code=None, company_name=None, ticker=None, form_types=None, filled_from_ts=None, filled_to_ts=None, page=None, include_files=None):
        params = {
            'cik_code': cik_code,
            'company_name': company_name,
            'ticker': ticker,
            'form_types': form_types,
            'filled_from_ts': filled_from_ts,
            'filled_to_ts': filled_to_ts,
            'page': page,
            'include_files': include_files
        }
        return self._send_request("/sec/archive", params)

    def get_time_series(self, publisher, ticker, interval, market=None, country=None, timezone=None, date=None, start_at=None, end_at=None, page=0, page_size=100, order="DESC", prepost=False):
        params = {
            'publisher': publisher,
            'ticker': ticker,
            'interval': interval,
            'market': market,
            'country': country,
            'timezone': timezone,
            'date': date,
            'start_at': start_at,
            'end_at': end_at,
            'page': page,
            'page_size': page_size,
            'order': order,
            'prepost': prepost
        }
        return self._send_request("/time_series", params)

    def get_trades(self, publisher, ticker, country=None, start_at=None, end_at=None, page=0, page_size=10, order="DESC"):
        params = {
            'publisher': publisher,
            'ticker': ticker,
            'country': country,
            'start_at': start_at,
            'end_at': end_at,
            'page': page,
            'page_size': page_size,
            'order': order
        }
        return self._send_request("/trades", params)

    def get_api_usage(self, product=None):
        params = {
            'product': product
        }
        return self._send_request("/api_usage", params)

    def get_publishers(self, code=None, page=0, page_size=100):
        params = {
            'code': code,
            'page': page,
            'page_size': page_size
        }
        return self._send_request("/publishers", params)

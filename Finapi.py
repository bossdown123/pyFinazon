import requests
import pandas as pd
class Finazon:

    BASE_URL = "https://api.finazon.io/v1.0"
    
    def __init__(self, api_key):
        self.api_key = api_key
        self._last_response = None
        self._last_method = None
        self._df_accessed = False

    
    def _send_request(self, endpoint, params={}):
        headers = {
            'accept': 'application/json',
            'Authorization': f"apikey {self.api_key}"
        }
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        self._last_response = response.json()
        self._last_method = endpoint
        return self._last_response
        
    @property
    def df(self):
        """Convert the last stored response to a DataFrame."""
        self._df_accessed = True
        if not self._last_response:
            raise ValueError("No recent API call data found!")

        data = self._last_response

        # Check the method name and handle the data accordingly
        if "/time_series" in self._last_method:
            tickers = [entry['ticker'] for entry in data]
            data_sets = [entry['data'] for entry in data]
            return self._time_series_df(data_sets, tickers)
        elif 'data' in data:
            return pd.DataFrame(data['data'])
        else:
            return pd.DataFrame(data)

    def __repr__(self):
        if not self._df_accessed:
            return str(self._last_response)
        return super().__repr__()

    def _time_series_df(self, data_sets, stock_labels, columns=['open','high','low','close','volume']):
        """
        Formats and concatenates multiple data sets along axis 1.

        Parameters:
        - data_sets: List of data sets (list of dictionaries)
        - stock_labels: List of stock labels (list of strings)

        Returns:
        - A formatted and concatenated DataFrame
        """

        formatted_dfs = []

        for data, label in zip(data_sets, stock_labels):
            df = pd.DataFrame(data)

            # Convert 't' to datetime format and set as index
            df['datetime'] = pd.to_datetime(df['t'], unit='s')
            df = df.drop(columns='t').set_index('datetime')

            # Set stock label as top-level column
            df.columns = pd.MultiIndex.from_product([[label], columns])

            formatted_dfs.append(df)

        # Concatenate along axis 1
        concatenated_df = pd.concat(formatted_dfs, axis=1).sort_index(ascending=True)

        return concatenated_df

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

    def get_time_series(self, publisher, tickers, interval, market=None, country=None, timezone=None, date=None, start_at=None, end_at=None, page=1, page_size=100, order="DESC", prepost=True):
        self._df_accessed = False
        aggregated_data = []
        
        for ticker in tickers:
            print(f"\nFetching data for {ticker}...")
            pages = []
            page = 1
            previous_last_t = None  # To store the last timestamp of the previous page
        
            while True:
                params = {
                    'publisher': publisher,
                    'ticker': ticker,
                    'interval': interval,
                    'market': market,
                    'country': country,
                    'timezone': 'utc',
                    'date': date,
                    'start_at': start_at,
                    'end_at': end_at,
                    'page': page,
                    'page_size': page_size,
                    'order': order,
                    'prepost': prepost
                }
                print(f"Sending request for page {page} with parameters: {params}")
                self._send_request("/time_series", params)
                data = self._last_response
                
                if not data['data']:  # break when there's no more data to paginate
                    print(f"No data returned for page {page}. Breaking loop.")
                    break

                current_first_t = data['data'][0]['t']
                current_last_t = data['data'][-1]['t']
                print(f"Page {page}: First timestamp = {current_first_t}, Last timestamp = {current_last_t}")

                if previous_last_t and previous_last_t == current_first_t:
                    print(f"Warning: First timestamp of page {page} matches the last timestamp of page {page-1}. Possible overlap.")
                
                pages.append(data['data'])
                previous_last_t = current_last_t

                # Check the last timestamp in the current page
                last_t = data['data'][-1]['t']
                if start_at and last_t <= start_at:
                    break

                # Break loop if data length is less than page_size
                if len(data['data']) < page_size:
                    break

                page += 1  # paginate to the next page

            # Aggregate the pages into a single list for the current ticker and append to aggregated_data
            aggregated_data.append({'ticker': ticker, 'data': [x for y in pages for x in y]})
        
        # Update the _last_response to be the aggregated data
        self._last_response = aggregated_data
        self.tstickers = tickers

        return self


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

# base.py

def get_ticker_snapshot(self, publisher, ticker, market=None, country=None):
    params = {
        'publisher': publisher,
        'ticker': ticker,
        'market': market,
        'country': country
    }
    return self._send_request("/ticker/snapshot", params)


def get_time_series(self, publisher, tickers, interval, market=None, country=None, timezone=None, date=None, start_at=None, end_at=None, page=1, page_size=100, order="DESC", prepost=True):
    from .core import to_epoch
    self._df_accessed = False
    aggregated_data = []
    opage = page
    if isinstance(tickers, str):
        tickers = [tickers]
    tickers=[ticker.upper() for ticker in tickers]
    for ticker in tickers:
        #print(f"\nFetching data for {ticker}...")
        pages = []
        page = opage
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
                'start_at': to_epoch(start_at) if start_at else None,
                'end_at': to_epoch(end_at) if end_at else None,
                'page': page,
                'page_size': page_size,
                'order': order,
                'prepost': prepost
            }
            #print(f"Sending request for page {page} with parameters: {params}")
            self._send_request("/time_series", params)
            data = self._last_response
            #print(data)

            if not data['data']:  # break when there's no more data to paginate
                print(f"No data returned for page {page}. Breaking loop.")
                break
            #print(start_at)

            
            current_first_t = data['data'][0]['t']
            current_last_t = data['data'][-1]['t']
            #print(f"Page {page}: First timestamp = {current_first_t}, Last timestamp = {current_last_t}")
            #if previous_last_t and previous_last_t == current_first_t:
                #print(f"Warning: First timestamp of page {page} matches the last timestamp of page {page-1}. Possible overlap.")

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
            if not start_at:
                break
        # Aggregate the pages into a single list for the current ticker and append to aggregated_data
        aggregated_data.append(
            {'ticker': ticker, 'data': [x for y in pages for x in y]})

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

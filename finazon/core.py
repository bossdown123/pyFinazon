# core.py

import requests
import pandas as pd
import datetime

from .base import get_ticker_snapshot, get_time_series, get_trades, get_api_usage, get_publishers


class Finazon:

    BASE_URL = "https://api.finazon.io/v1.0"

    def __init__(self, api_key):
        self.api_key = api_key
        self._last_response = None
        self._last_method = None
        self._df_accessed = False
        self.get_ticker_snapshot = get_ticker_snapshot.__get__(self)
        self.get_time_series = get_time_series.__get__(self)
        self.get_trades = get_trades.__get__(self)
        self.get_api_usage = get_api_usage.__get__(self)
        self.get_publishers = get_publishers.__get__(self)

    def _send_request(self, endpoint, params={}):
        headers = {
            'accept': 'application/json',
            'Authorization': f"apikey {self.api_key}"
        }
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        
        # Check for a 401 status code
        if response.status_code == 401:
            error_response = response.json()
            error_message = error_response['error']['message']
            raise Exception(f"Error {response.status_code}: {error_message}. More info: {error_response['error']['more_info']}")

        self._last_response = response.json()
        self._last_method = endpoint
        return self._last_response

    @property
    def raw(self):
        """Return the raw API response."""
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

    def _time_series_df(self, data_sets, stock_labels, columns=['open', 'high', 'low', 'close', 'volume']):
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
            #print(data)
            df = pd.DataFrame(data)
            #print(df)
            # Convert 't' to datetime format and set as index
            df['datetime'] = pd.to_datetime(df['t'], unit='s')
            df = df.drop(columns='t').set_index('datetime')

            # Set stock label as top-level column
            df.columns = pd.MultiIndex.from_product([[label], columns])

            formatted_dfs.append(df)

        # Concatenate along axis 1
        concatenated_df = pd.concat(
            formatted_dfs, axis=1).sort_index(ascending=True)

        return concatenated_df
def to_epoch(value):
    if isinstance(value, datetime.datetime):
        # Convert datetime to epoch
        return int(value.timestamp())
    elif isinstance(value, int):
        # Already in epoch format
        return value
    else:
        raise ValueError("Unsupported type for conversion to epoch")
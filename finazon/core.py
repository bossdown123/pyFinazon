# core.py

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

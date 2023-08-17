[![Upload Python Package](https://github.com/bossdown123/pyFinazon/actions/workflows/python-publish.yml/badge.svg)](https://github.com/bossdown123/pyFinazon/actions/workflows/python-publish.yml) [![Python package](https://github.com/bossdown123/pyFinazon/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/bossdown123/pyFinazon/actions/workflows/python-package.yml)


# pyFinazon

A Python package for fetching financial data from the Finazon API.

## Installation

```bash
!pip install pyFinazon
```
## Example usage
```py
from finazon import Finazon
api=Finazon(api_key='your api key')
data=api.get_time_series('sip', ['AAPL','tsla'], '1d',page=4)
data.df
```

| datetime            |   ('AAPL', 'open') |   ('AAPL', 'high') |   ('AAPL', 'low') |   ('AAPL', 'close') |   ('AAPL', 'volume') |   ('TSLA', 'open') |   ('TSLA', 'high') |   ('TSLA', 'low') |   ('TSLA', 'close') |   ('TSLA', 'volume') |
|:--------------------|-------------------:|-------------------:|------------------:|--------------------:|---------------------:|-------------------:|-------------------:|------------------:|--------------------:|---------------------:|
| 2022-06-01 04:00:00 |                  0 |                  0 |                 0 |                   0 |                    0 |                  0 |                  0 |                 0 |                   0 |                    0 |
| 2022-06-02 04:00:00 |                  0 |                  0 |                 0 |                   0 |                    0 |                  0 |                  0 |                 0 |                   0 |                    0 |
| 2022-06-03 04:00:00 |                  0 |                  0 |                 0 |                   0 |                    0 |                  0 |                  0 |                 0 |                   0 |                    0 |
| 2022-06-06 04:00:00 |                  0 |                  0 |                 0 |                   0 |                    0 |                  0 |                  0 |                 0 |                   0 |                    0 |
| 2022-06-07 04:00:00 |                  0 |                  0 |                 0 |                   0 |                    0 |                  0 |                  0 |                 0 |                   0 |                    0 |

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
| 2022-06-01 04:00:00 |            149.9   |            151.74  |            147.68 |              148.71 |          7.42866e+07 |            755.16  |             771.98 |           730.92  |              740.37 |          2.57493e+07 |
| 2022-06-02 04:00:00 |            147.83  |            151.27  |            146.86 |              151.21 |          7.23481e+07 |            732.47  |             792.63 |           726.2   |              775    |          3.11577e+07 |
| 2022-06-03 04:00:00 |            146.9   |            147.97  |            144.46 |              145.38 |          8.85703e+07 |            729.675 |             743.39 |           700.253 |              703.55 |          3.74646e+07 |
| 2022-06-06 04:00:00 |            147.03  |            148.569 |            144.9  |              146.14 |          7.15984e+07 |            733.06  |             734.6  |           703.05  |              714.84 |          2.80682e+07 |
| 2022-06-07 04:00:00 |            144.345 |            149     |            144.1  |              148.71 |          6.78082e+07 |            702     |             719.99 |           690.28  |              716.66 |          2.42695e+07 |

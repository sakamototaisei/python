import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd


company_number = input('銘柄コードを入力してください: ')
interval = int(input('調べる期間を数字で入力してください: '))
my_share = share.Share(company_number+'.T')
symbol_data = None
try:
    symbol_data = my_share.get_historical(
    share.PERIOD_TYPE_YEAR, interval,
    share.FREQUENCY_TYPE_DAY, 1)
except YahooFinanceError as e:
    print(e.message)
    sys.exit(1)
df = pd.DataFrame(symbol_data)
df["datetime"] = pd.to_datetime(df.timestamp, unit="ms")
print(df.head())
print(df.tail())
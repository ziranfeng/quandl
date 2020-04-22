import logging
import yfinance as yf

from yitian.datasource import *

logging.basicConfig(filename=ETL_LOG, level=logging.INFO)


def yfinance_data_api(ticker, period, interval,
                      group_by='ticker', auto_adjust=True, prepost=True, threads=True, proxy=None):

    try:
        data_pd = yf.download(  # or pdr.get_data_yahoo(...
            # tickers list or string as well
            tickers=ticker,

            # use "period" instead of start/end
            # valid periods: 1d, 5d,1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
            # (optional, default is '1mo')
            period=period,

            # fetch data by interval (including intraday if period < 60 days)
            # valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
            # (optional, default is '1d')
            interval=interval,

            # group by ticker (to access via data['SPY'])
            # (optional, default is 'column')
            group_by=group_by,

            # adjust all OHLC automatically
            # (optional, default is False)
            auto_adjust=auto_adjust,

            # download pre/post regular market hours data
            # (optional, default is False)
            prepost=prepost,

            # use threads for mass downloading? (True/False/Integer)
            # (optional, default is True)
            threads=threads,

            # proxy URL scheme use use when downloading?
            # (optional, default is None)
            proxy=proxy
        )

        data_pd.reset_index(inplace=True)

        return data_pd

    except Exception as err:
        print(err)
        logging.error(err, exc_info=True)

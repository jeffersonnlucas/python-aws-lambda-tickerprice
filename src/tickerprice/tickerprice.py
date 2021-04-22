import json
import datetime
import requests
import logging
import pandas as pd

from datetime import timezone
from pandas.io.json import json_normalize

# Logger settings - CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Set UTC Timestamp
dt = datetime.datetime.now(timezone.utc)
url = "https://api.binance.com/api/v3/ticker/price"

def lambda_handler(event, context):
    print(f'Initialize get price tickers: {dt}')

    df = pd.read_json(url)
    df["timestamp"] = dt.timestamp()

    print(f'Finalize get price tickers.')

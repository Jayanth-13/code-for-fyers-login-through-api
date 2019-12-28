import pandas as pd
import numpy as np
pip install fyers_api
pip install tornado     # Tornado is a python web framework and asynchronous networking library
from fyers_api import fyersModel 
from fyers_api import accessToken
api_id="XXXXXX"   
api_secret="XXXXXXX"
app_session=accessToken.SessionModel(api_id,api_secret)
response = app_session.auth()
print(response)   # We are printing response where authorization code is observed.

authorization_code = "  XXXXXXXXXXXXXXXXXXXXXXXXXXX"
app_session.set_token(authorization_code)
print(app_session.generate_token())   # you will get an URL, by clicking on it you will get an access token.

access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
is_async = False
fyers = fyersModel.FyersModel(is_async)
print(fyers.get_profile(token = token)  #Profile of an trader shown up here

print(fyers.holdings(token = token))    # Holdings of an trader will be shown up here

#Placing an order.
fyers.place_orders(token = token, data = {"symbol" : "XXXX", "price":"XX", qty="10", "type="1", "side": 1, "productType":"INTRADAY", "triggerPrice":"XXX", "limitPrice":"XX", "stopPrice":"XX", "stopLoss":"XX", "takeProfit":"XX"})

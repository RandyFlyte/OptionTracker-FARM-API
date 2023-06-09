import tda.client
from tda import auth, client
import json, os
from dotenv import load_dotenv

load_dotenv()

token_path = os.getenv('TOKEN_PATH')
api_key = os.getenv('API_KEY')
redirect_uri = os.getenv('REDIRECT_URI')

try:
    c = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    from selenium import webdriver

    with webdriver.Chrome() as driver:
        c = auth.client_from_login_flow(
            driver, api_key, redirect_uri, token_path)

r = c.get_option_chain('WISH', strike=1, contract_type=tda.client.Client.Options.ContractType.CALL)
data = r.json()
print(data)
print(data['underlyingPrice'])
# iterate through each option object in the callExpDateMap dictionary
for date in data['callExpDateMap']:
    for strike_price in data['callExpDateMap'][date]:
        for option in data['callExpDateMap'][date][strike_price]:
            # check if the symbol of the option matches the target symbol
            if option['symbol'] == 'WISH_042123C1':
                # do something with the matching option object
                print(option['bid'])
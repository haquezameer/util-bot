import requests

URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=INR'


def getBitcoinPrice():
    res = requests.get(URL)
    json_res = res.json()
    result = json_res[0]
    name = result['name']
    symbol = result['symbol']
    price_usd = result['price_usd']
    price_inr = result['price_inr']
    return '<Name: ' + name + '> ' + '<Symbol: ' + symbol + '> ' + '<Price in INR: ' + price_inr + '> ' \
        + '<Price in USD: ' + price_usd + '>'

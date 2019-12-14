import requests
import json
import wget
import os

url = "https://api.coingecko.com/api/v3/simple/price?ids=WAX&vs_currencies=BTC%2CUSD"

payload = "{\"limit\":\"200\",\"json\":true}"
headers = {
    'accept': "application/json",
    'content-type': "application/json"
    }

response = requests.request("GET", url, data=payload, headers=headers)


parsed = json.loads(response.text)


waxusd = int(parsed["wax"]["usd"] * 10000)
waxbtc = int(parsed["wax"]["btc"]*100000000)

print('WaxBTC = %d' % (waxbtc))
print('WaxUSD = %d' % (waxusd))

os.system('cleos wallet unlock --password  [update the wallet password here] > /dev/null 2> /dev/null')


test = ('cleos -u [update URL to API endpoint] push action delphioracle write \'{"owner":"<ACCOUNT_NAME>", "quotes": [{"value":"%d", "pair":"waxpusd"},{"value":"%d", "pair":"waxpbtc"}]}\' -p <ACCOUNT_NAME>@oraclepricefe') % (waxusd, waxbtc)



os.system(test)

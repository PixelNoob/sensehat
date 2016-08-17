from sense_hat import SenseHat
sense = SenseHat()
from urllib.request import urlopen
import json

url = urlopen('https://poloniex.com/public?command=returnTicker').read()
result = json.loads(url)

SBD = result['BTC_SBD']['last']
BTC = result['USDT_BTC']['last']
Steem = result['BTC_STEEM']['last']
SBD_USD = float(SBD) * float(BTC)

while True:
  try:
    sense.show_message("BTC " + BTC, text_colour=[255, 215, 0])
    sense.show_message("Steem " + Steem, text_colour=[7, 24, 138])
    sense.show_message("SBD " + '{0:f}'.format(SBD_USD), text_colour=[4, 112, 22])
  except:
    sense.show_message("failed to retrieve feed")

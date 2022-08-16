import discord
from discord.ext import commands
from requests import Request, Session
import json
import pprint

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

parameters = {
    'slug': 'ethereum',
    'convert': 'USD'
}
# bitcoin - 1
# ethereum - 1027

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'c96b8579-7587-4860-8b92-258d45329733'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params = parameters)
pprint.pprint(response.text)

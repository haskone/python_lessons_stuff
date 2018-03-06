import requests
from bs4 import BeautifulSoup

ycomb = "https://news.ycombinator.com/"
soup = BeautifulSoup(requests.get(ycomb).content)

print(soup.findAll("a", {"class": "storylink"})[0])

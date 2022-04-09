from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://kuathletics.com/sports/mbball/roster/'

page = requests.get(url)
names = []
soup = BeautifulSoup(page.content, 'html.parser')
players = soup.find_all('div', class_="inner")
number = 1
for player in players:
    name = player.find('a', itemprop="url").text
    print(number)
    print(name)
    number += 1

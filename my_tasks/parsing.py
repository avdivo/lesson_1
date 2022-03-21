import requests
from bs4 import BeautifulSoup

url = 'https://remontnoutbukoff.ru/'
response = requests.get(url).content
soup = BeautifulSoup(response, "html.parser")

res = []
for link in soup.find_all('h3'):
    res.append(link.get_text())
print(res)
from bs4 import BeautifulSoup
import requests
url = 'https://www.bbc.com/news'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('div', {'class': 'gs-o-media-island'})
print([i.find('img')['src'] for i in links])

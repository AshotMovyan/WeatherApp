"""+++++++++++++++"""
from bs4 import BeautifulSoup
import requests

def parse():
    URL = 'https://weather.com/weather/today/l/e958ec105aef48bbab18247e979b1e10a163e36cab17882a4c901f2b2cb1954f'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    proxy = {
        'http': 'http://proxy.hf.am:3128',
        'https': 'http://proxy.hf.am:3128'
    }
    response = requests.get(URL, headers = HEADERS, proxies=proxy)
    soup = BeautifulSoup(response.content, 'html.parser')

    def weatherHourly():



        todayDiv3 = soup.findAll('li', class_ = 'Column--column--2bRa6')
        data3 = []
        kl = []

        for i in todayDiv3:
            data3.append({
                'forcast': [i.find('span', class_='Ellipsis--ellipsis--lfjoB').get_text(strip=True),
                            i.find('div', class_='Column--temp--2v_go').get_text(strip=True),
                            i.find('span', class_='Column--precip--2H5Iw').get_text(strip=True)]
            })

            # data3.append(i.find('span', class_='Ellipsis--ellipsis--lfjoB').get_text(strip=True))
            # data3.append(i.find('div', class_='Column--temp--2v_go').get_text(strip=True))

        # print("LIST -", data3)
        for i in data3:
            # print(i['forcast'])


            print(i['forcast'][0], i['forcast'][1], i['forcast'][2])



    weatherHourly()

parse()

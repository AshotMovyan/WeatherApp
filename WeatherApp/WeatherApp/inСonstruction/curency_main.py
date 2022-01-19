import eel
import requests
from bs4 import BeautifulSoup

eel.init('Interface')

@eel.expose
def get_cur(a, b, c):
    cur = a
    from_ = b
    to = c

    URL = 'https://www.xe.com/currencyconverter/convert/?Amount=' + cur + '&From=' + from_ + '&To=' + to
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    proxy = {
        'http': 'http://proxy.hf.am:3128',
        'https': 'http://proxy.hf.am:3128'
    }
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')

    print(URL)

    mainAll = soup.findAll('main', class_='tab-box__ContentContainer-sc-28io75-3 jFGFzo')
    main = []

    for i in mainAll:
        main.append(i.find('p', class_='result__ConvertedText-sc-1bsijpp-0 gwvOOF').get_text(strip=True))
        main.append(i.find('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod').get_text(strip=True))
        main.append(i.findAll('p', attrs={'class': None})[0].get_text(strip=True))
        main.append(i.findAll('p', attrs={'class': None})[1].get_text(strip=True))


    convert1 = []
    convert2 = []

    table = soup.findAll('table', attrs={'class': 'currency-conversion-tables__ConverterTable-sc-3fg8ob-5 jESrzS'})[0]
    table_body2 = table.find('tbody')


    table_conv2 = soup.findAll('table', attrs={'class': 'currency-conversion-tables__ConverterTable-sc-3fg8ob-5 jESrzS'})[1]
    table_convbody = table_conv2.find('tbody')

    rows2 = table_convbody.find_all('tr')
    for row in rows2:
        cols2 = row.find_all('td')
        cols2 = [ele2.text.strip() for ele2 in cols2]
        convert2.append([ele2 for ele2 in cols2 if ele2])


    rows1 = table_body2.find_all('tr')
    for row in rows1:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        convert1.append([ele for ele in cols if ele])


    all_ = main + convert1 + convert2

    print(all_)
    return all_

eel.start('currency.html', size=(500, 500))
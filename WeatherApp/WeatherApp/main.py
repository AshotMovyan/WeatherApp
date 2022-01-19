#!/usr/bin/python3
# -*- coding: utf-8 -*-

import eel
#import pyowm
import Weather_today
import news

# import Client
import eel
import requests
from bs4 import BeautifulSoup
eel.init("Interface")

DISCONNECT_MESSAGE = "!DISCONNECT"

pars = Weather_today.Parse()
news_ = news.defparse()

@eel.expose
def get_weather(place):
    global pars
    pars = Weather_today.Parse()
    # print(pars.Weather('C'))

    return pars.Weather('C', place)


@eel.expose
def get_divice_date():
    try:
        val = Client.send('')
        val = [val[2:7] + ' %', val[7:13] + ' °C']
        print(val)
        return val

    except ConnectionRefusedError:
        print('Server dont connect')


@eel.expose
def get_weather_ten(arg):
    global pars
    # print(pars.Weather_Ten_Day('C', arg))
    return pars.Weather_Ten_Day('C', arg)


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
    stats_datas = []

    table = soup.findAll('table', attrs={'class': 'currency-conversion-tables__ConverterTable-sc-3fg8ob-5 jESrzS'})[0]
    table_body2 = table.find('tbody')


    table_conv2 = soup.findAll('table', attrs={'class': 'currency-conversion-tables__ConverterTable-sc-3fg8ob-5 jESrzS'})[1]
    table_convbody = table_conv2.find('tbody')

    firstconvt = soup.findAll('h3', class_='heading__Heading1-n07sti-0 heading__Heading3-n07sti-2 iXbZUl')[0].get_text(strip=True)

    rows2 = table_convbody.find_all('tr')
    for row in rows2:
        cols2 = row.find_all('td')
        cols2 = [ele2.text.strip() for ele2 in cols2]
        convert2.append([ele2 for ele2 in cols2 if ele2])


    secconvt = soup.findAll('h3', class_='heading__Heading1-n07sti-0 heading__Heading3-n07sti-2 iXbZUl')[1].get_text(strip=True)

    rows1 = table_body2.find_all('tr')
    for row in rows1:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        convert1.append([ele for ele in cols if ele])


    table = soup.find('table', attrs={'class': 'stats-table__ConverterTable-sc-1uiw32l-1 bqDjxi'})
    table_body = table.find('tbody')

    statstext = soup.find('h2', class_='heading__Heading1-n07sti-0 heading__Heading2-n07sti-1 iXbZUl').get_text(strip=True)
    rowst = table_body.find_all('tr')
    for strParseow in rowst:
        colst = strow.find_all('td')
        colst = [eles.text.strip() for eles in colst]
        stats_datas.append([eles for eles in colst if eles])
    stats_datas.append(statstext)
    convert2.append(secconvt)
    convert2.append(firstconvt)

    all_ = main + convert1 + convert2 + stats_datas

    print(all_)
    return all_

@eel.expose
def get_News(a):
    global news_
    return news_.news(a)

if __name__ == "__main__":
    eel.start("mainpage.html", size=(700, 600))

from bs4 import BeautifulSoup
import requests

from googlesearch import search


class Parse:
    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        self.proxy = {
            'http': 'http://proxy.hf.am:3128',
            'https': 'http://proxy.hf.am:3128'
        }
        
        self.today = []
        self.comps = []
        self.comp = None
        self.data = []
        self.datas = []
        self.kl = []


    def Weather_Ten_Day(self, f_c, ten_weath):
        self.ten_query = 'weather ' + ten_weath + ' 10 day ' + 'site:weather.com'
        for self.i in search(self.ten_query, tld="co.in", num=1, stop=1, pause=0):
            self.url_ten = self.i
        self.response_ten = requests.get(self.url_ten, headers=self.headers)
        self.soup_ten = BeautifulSoup(self.response_ten.content, 'html.parser')

        self.todayDiv3 = self.soup_ten.findAll('summary',
                                               class_='Disclosure--Summary--AvowU DaypartDetails--Summary--2nJx1 Disclosure--hideBorderOnSummaryOpen--LEvZQ')
        self.data3 = []

        for ij in self.todayDiv3:
            if f_c == 'C':
                self.data3.append(ij.find('h2', class_='DetailsSummary--daypartName--1Mebr').get_text(strip=True))
                self.data3.append(str(((int((''.join(
                    (ij.find('div', class_='DetailsSummary--temperature--3FMlw').get_text(strip=True)).split(
                        '°'))).split('/')[0]) - 32) * 5 // 9)) +
                '°/' + str(((int((''.join(
                    (ij.find('div', class_='DetailsSummary--temperature--3FMlw').get_text(strip=True)).split(
                        '°'))).split('/')[1]) - 32) * 5 // 9)) + '°')
                self.data3.append(ij.find('span', class_='DetailsSummary--extendedData--aaFeV').get_text(strip=True))
                self.data3.append(ij.find('div', class_='DetailsSummary--precip--2ARnx').get_text(strip=True))
                self.data3.append(ij.find('span', class_='Wind--windWrapper--1Va1P undefined').get_text(strip=True))

        return self.data3

    def Weather(self, tem_type, query_arg):
        print(query_arg)
        self.query = 'weather ' + query_arg

        for self.j in search(self.query, tld="co.in", num=1, stop=1, pause=0):
            self.url = self.j

        try:
            self.response = requests.get(self.url, headers=self.headers)
        except:
            self.proxy = {
                'http': 'http://proxy.hf.am:3128',
                'https': 'http://proxy.hf.am:3128'
            }
            self.response = requests.get(self.url, headers=self.headers, proxies=self.proxy)
        print(self.url)

        # self.response = requests.get(self.url, headers=self.headers, proxies=self.proxy)
        # self.response = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

        self.items = self.soup.findAll('div', class_='CurrentConditions--CurrentConditions--2_Nmm')
        self.todayDiv = self.soup.findAll('div',
                                          class_='ListItem--listItem--1r7mf WeatherDetailsListItem--WeatherDetailsListItem--3w7Gx')
        self.todayDivs = self.soup.findAll('li', class_='Column--column--2bRa6')

        for self.item in self.items:
            self.comps.append({

                'City': self.item.find('h1', class_='CurrentConditions--location--1Ayv3').get_text(strip=True),
                'Time': self.item.find('div', class_="CurrentConditions--timestamp--1SWy5").get_text(strip=True),
                'Temp': self.item.find('span', class_="CurrentConditions--tempValue--3KcTQ").get_text(strip=True),
                'vic': self.item.find('div', class_="CurrentConditions--phraseValue--2xXSr").get_text(strip=True),
                'chan': self.item.find('div', class_="CurrentConditions--tempHiLoValue--A4RQE").get_text(
                    strip=True),
            })

            for self.comp in self.comps:
                if tem_type == 'C':
                    try:
                        self.cels__aal = self.comp['Temp'].split('°')
                        self.cels__aal = (int(''.join(self.cels__aal)) - 32) * 5 // 9
                        self.fc__all = [self.comp['City'], self.comp['Time'], str(self.cels__aal) + '°',
                                        self.comp['vic'], str(((int((''.join(
                                (self.comp['chan']).split(
                                    '°'))).split('/')[0]) - 32) * 5 // 9)) +
                                        '°/' + str(((int((''.join(
                                (self.comp['chan']).split(
                                    '°'))).split('/')[1]) - 32) * 5 // 9)) + '°']
                    except:
                        self.cels__aal = self.comp['Temp'].split('°')
                        self.cels__aal = (int(''.join(self.cels__aal)) - 32) * 5 // 9
                        self.fc__all = [self.comp['City'], self.comp['Time'], str(self.cels__aal) + '°',
                                        self.comp['vic'], '--' +
                                        '/' + str(((int((''.join(
                                (self.comp['chan']).split(
                                    '°'))).split('/')[1]) - 32) * 5 // 9)) + '°']
                    # return self.fc__all


                else:
                    self.far__aal = self.comp['Temp'].split('°')
                    self.far__aal = ''.join(self.far__aal)
                    self.fc__all = [self.comp['City'], self.comp['Time'], str(self.far__aal) + 'F°',
                                    self.comp['vic'], self.comp['chan']]
                    # return self.fc__all

        for self.i in self.todayDiv:
            self.data.append(
                self.i.find('div', class_='WeatherDetailsListItem--wxData--23DP5').get_text(strip=True)
            )

        if tem_type == 'C':
            self.data[0] = '--/' + str((int(self.data[0][4:-1]) - 32) * 5 // 9) + '°'
            self.data[3] = str((int(self.data[3][0:-1]) - 32) * 5 // 9) + '°'

        for self.i in self.todayDivs:
            self.datas.append({
                'forcast': [self.i.find('span', class_='Ellipsis--ellipsis--lfjoB').get_text(strip=True),
                            self.i.find('div', class_='Column--temp--2v_go').get_text(strip=True),
                            self.i.find('span', class_='Column--precip--2H5Iw').get_text(strip=True)]
            })

        for self.i in self.datas:
            self.data.append(self.i['forcast'][0])
            if tem_type == 'C':
                self.data_c = self.i['forcast'][1].split('°')
                try:
                    self.data_c = (int(''.join(self.data_c)) - 32) * 5 // 9
                except:
                    self.data.append(self.i['forcast'][1])
                    continue
                self.data.append(str(self.data_c) + '°')

            else:
                self.data.append(self.i['forcast'][1])

            self.data.append(self.i['forcast'][2])

        self.general = self.fc__all + self.data

        self.wind = self.general[6]
        del self.general[6]

        self.wind = self.wind[14:]

        self.general.insert(6, self.wind)
        return self.general

# parse = Parse('vanadzor')
# print(parse.Weather('C'))

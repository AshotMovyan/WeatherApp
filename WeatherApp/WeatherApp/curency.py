from bs4 import BeautifulSoup
import requests
import time
# cur = input("cur - ")
# from_ = input('From - ').upper()
# to = input("TO - ").upper()

class Curency:

    def __init__(self):
        self.cur = '50'
        self.from_ = 'USD'
        self.to = 'AMD'

        self.URL = 'https://www.xe.com/currencyconverter/convert/?Amount=' + self.cur + '&From=' + self.from_ + '&To=' + self.to
        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
        }
        self.proxy = {
            'http': 'http://proxy.hf.am:3128',
            'https': 'http://proxy.hf.am:3128'
        }
        self.response = requests.get(self.URL, headers = self.HEADERS, proxies=self.proxy)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

        print(self.URL)
        self.statsAll = self.soup.findAll('div', class_ = 'stats-table__TableContainer-sc-1uiw32l-0 koWqDE')
        self.convert1All = self.soup.findAll('table', class_='currency-conversion-tables__ConverterTable-sc-3fg8ob-5 jESrzS')
        self.convertText = self.soup.findAll('div', class_='currency-conversion-tables__TableHeadingWrapper-sc-3fg8ob-4 jPkXeQ')

        self.stats = []
        self.table = self.soup.find('table', attrs={'class':'stats-table__ConverterTable-sc-1uiw32l-1 bqDjxi'})
        self.table_body = self.table.find('tbody')

        self.convert = []
        self.table = self.soup.find('table',
                               attrs={'class': 'currency-conversion-tables__ConverterTable-sc-3fg8ob-5 jESrzS'})
        self.table_body = self.table.find('tbody')

        self.convert2 = []
        self.table = self.soup.findAll('table', attrs={'class': 'currency-conversion-tables__ConverterTable-sc-3fg8ob-5 jESrzS'})[
            1]
        self.table_body = self.table.find('tbody')

    def get_Curency(self):
        self.rows = self.table_body.find_all('tr')
        for self.row in self.rows:
            self.colss = self.row.find_all('th')
            self.cols = self.row.find_all('td')
            self.cols = [self.ele.text.strip() for self.ele in self.cols]
            self.stats.append([self.ele for self.ele in self.cols if self.ele]) # Get rid of empty values


        self.rows = self.table_body.find_all('tr')
        for self.row in self.rows:
            self.cols = self.row.find_all('td')
            self.cols = [self.ele.text.strip() for self.ele in self.cols]
            self.convert.append([self.ele for self.ele in self.cols if self.ele]) # Get rid of empty values


        self.rows = self.table_body.find_all('tr')
        for self.row in self.rows:
            self.cols = self.row.find_all('td')
            self.cols = [self.ele.text.strip() for self.ele in self.cols]
            self.convert2.append([self.ele for self.ele in self.cols if self.ele]) # Get rid of empty values

        return "stats ===== ", self.stats, "Convert 1 ===== ", self.convert, "Convert 2 =====", self.convert2

parse = Curency()
print(parse.get_Curency())






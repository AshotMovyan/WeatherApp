from bs4 import BeautifulSoup
import requests

class defparse:
    def __init__(self):
       global HEADERS, proxy, response, soup
       self.HEADERS = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
       }
       self.proxy = {
           'http': 'http://proxy.hf.am:3128',
           'https': 'http://proxy.hf.am:3128'
       }
    def latest(self):
        self.URL2 = 'https://www.google.com/search?q=latest&safe=active&biw=1920&bih=1057&tbm=nws&sxsrf=ALeKk03eKuxJCGqqZGUWb83q5KMNNSlaYg%3A1620380809092&ei=iQyVYJGJBZWbkgXej5KYAw&oq=latest&gs_l=psy-ab.3...1766.1966.0.2131.2.2.0.0.0.0.132.132.0j1.1.0....0...1c.1.64.psy-ab..1.0.0....0.16drBWAWCwY'


        self.response = requests.get(self.URL, headers=self.HEADERS)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def news(self, a):
        self.URL = 'https://www.google.com/search?q=' + a + 'news&safe=active&hl=en&sxsrf=ALeKk03LojYRREKWIOCm2fxHEPPqMuNX6w:1620337227125&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjS2NrGgrbwAhUtiYsKHSPTA_UQ_AUoAXoECAQQAw&biw=1680&bih=939'
        self.response = requests.get(self.URL, headers=self.HEADERS)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

        print(self.URL)
        self.newsList = self.soup.findAll('div', class_ = 'yr3B8d KWQBje')
        self.news_dat = []

        for self.i in self.newsList:
            self.news_dat.append(self.i.find('div', class_='XTjFC WF4CUc').get_text(strip=True))
            self.news_dat.append(self.i.find('div', class_='JheGif nDgy9d').get_text(strip=True))
            self.news_dat.append(self.i.find('div', class_='Y3v8qd').get_text(strip=True))
            self.news_dat.append(self.i.find('span', class_='WG9SHc').get_text(strip=True))


        for self.i in self.news_dat:
            print(self.i)

        return self.news_dat


cl = defparse()
# cl.news("london")
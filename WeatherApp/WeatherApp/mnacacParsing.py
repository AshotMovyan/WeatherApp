from bs4 import BeautifulSoup
import requests

URL = 'https://weather.com/weather/today/l/e958ec105aef48bbab18247e979b1e10a163e36cab17882a4c901f2b2cb1954f'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
proxy = {
    'http': 'http://proxy.hf.am:3128',
    'https': 'http://proxy.hf.am:3128'
}
# response = requests.get(URL, headers = HEADERS)
response = requests.get(URL, headers = HEADERS, proxies=proxy)

soup = BeautifulSoup(response.content, 'html.parser')

def weatherHourly():

    # todayDiv1 = soup.findAll('div', class_='appWrapper DaybreakLargeScreen LargeScreen DaybreakLargeScreen--appWrapper--3sKDm gradients--rainyDay--NgsT4 gradients--rainyDay-top--1rAbx')
    # # a = tempa.next_element
    # data = []
    # for i in todayDiv1:
    #     data.append({
    #         'temp': i.find('span', class_ = 'TodayDetailsCard--feelsLikeTempValue--2aogo').get_text(strip=True),
    #         'feelsL': i.find('span', class_ = 'TodayDetailsCard--feelsLikeTempLabel--1i4BV').get_text(strip=True)
    #
    #     })
    #
    # todayDiv2 = soup.findAll('div', class_ = 'TodayDetailsCard--detailsContainer--1tqay')
    # data2 = []
    # for i in todayDiv2:
    #     data2.append({
    #         'hiLo': i.find('div', class_ = 'WeatherDetailsListItem--wxData--23DP5').get_text(strip=True),
    #         'humidity': i.find('span', class_ = 'Wind--windWrapper--1Va1P undefined').get_text(strip=True),
    #         'moon': i.find('div', class_ = 'ListItem--listItem--1r7mf WeatherDetailsListItem--WeatherDetailsListItem--3w7Gx').get_text(strip=True),
    #     })

    # b = soup.select('span', class_ = 'Wind--windWrapper--1Va1P undefined')
    # for i in z:
    #     print(i.text)

    todayDiv = soup.findAll('div', class_ = 'ListItem--listItem--1r7mf WeatherDetailsListItem--WeatherDetailsListItem--3w7Gx')
    data = []
    for i in todayDiv:
        data.append(
            i.find('div', class_='WeatherDetailsListItem--wxData--23DP5').get_text(
                             strip=True),

        )

    print("LIST -", data)

    print("High / Low - ", data[0])
    print("Wind - ", data[1])
    print("Humidity - ", data[2])
    print("Dew Point - ", data[3])
    print("Pressure- ", data[4])
    print("UV Index - ", data[5])
    print("Visibility - ", data[6])
    print("Moon Phase - ", data[7])

    return data



weatherHourly()


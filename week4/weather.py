
# 기상청 홈페이지의 '도시별 현재 날씨' 자료에서 지역명, 기온, 습도, 풍향 데이터 크롤링 해오기


import requests                
from bs4 import BeautifulSoup  
import csv

class WeatherScraper() :
    
    def __init__(self) : 
        self.url = "http://www.kma.go.kr/weather/observation/currentweather.jsp"

    def getHTML(self) :
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        return soup
    
    def getWeatherInfo(self, soup):
        weathertable = soup.find('table', class_ = 'table_develop3' )
        weatherinfo=[]
        for tr in weathertable.find_all('tr'): # 모든 tr 태그 찾기
            tds = list(tr.find_all('td')) # 모든 td 태그 찾기
            for td in tds:                
                if td.find('a'):             
                    Point = td.find('a').text # 지역명
                    Temperature = tds[5].text # 기온
                    Humidity = tds[10].text # 습도
                    WindDirection = tds[11].text  # 풍향    
                    weatherinfo.append([Point, Temperature, Humidity, WindDirection]) # 날씨정보리스트에 추가

        return weatherinfo
    

    
    def writeCSV(self,weatherinfo) :
        file = open('weather.csv','a', newline='')
        wr = csv.writer(file)
        for i in weatherinfo:                                        
            wr.writerow([i])
        
        file.close()

    def scrap(self) :
        

        file = open('weather.csv','w', newline='')
        wr = csv.writer(file)
        wr.writerow(["Point", "Temperature", "Humidity", "WindDirection"])
        file.close()
        
        soup = self.getHTML()
        weatherinfo = self.getWeatherInfo(soup)
        self.writeCSV(weatherinfo)



if __name__ == "__main__":
    weatherscraper = WeatherScraper()
    weatherscraper.scrap()
    
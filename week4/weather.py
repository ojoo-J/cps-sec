

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
        for tr in weathertable.find_all('tr'):
            tds = list(tr.find_all('td'))
            for td in tds:                
                if td.find('a'):             
                    Point = td.find('a').text
                    Temperature = tds[5].text
                    Humidity = tds[10].text
                    WindDirection = tds[11].text      
                    weatherinfo.append([Point, Temperature, Humidity, WindDirection])

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
    
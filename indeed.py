import requests
from bs4 import BeautifulSoup
import csv

class Scraper() : #OK
    
    def __init__(self) : 
        self.url = "http://kr.indeed.com/jobs?q=python&limit=50"

    def getHTML(self,cnt) :
        res = requests.get(self.url + "&start=" + str(cnt*50))

        if res.status_code != 200 :
            print("request error : ", res.status_code)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")

        return soup

    def getPages(self, soup) :
        pages = soup.select(".pagination > a")

        return len(pages)
    
    def getCards(self, soup, cnt) : #OK
        jobCards = soup.find_all("div", class_ = "jobsearch-SerpJobCard")

        jobID = []
        jobTitle = []
        jobLocation = []

        for j in jobCards :
            jobID.append("http://kr.indeed.com/viewjob?jk=" + j["data-jk"])
            jobTitle.append(j.find("a").text.replace("\n", ""))
            if j.find("div", class_ = "location") != None :
                jobLocation.append(j.find("div", class_ = "location").text)
            elif j.find("span", class_ = "location") != None :
                jobLocation.append(j.find("span", class_ = "location").text)
        
        self.writeCSV(jobID, jobTitle, jobLocation, cnt)

    def writeCSV(self, ID, Title, Location, cnt) : #OK
        file = open('indeed.csv','a', newline='') #a는 append, w는 새로 쓰여짐

        wr = csv.writer(file)
        for i in range(len(ID)) : # 길이는 어차피 다 같으니까 셋 중 아무거나 하나
            wr.writerow([str(i + 1 + (cnt*50)), ID[i], Title[i], Location[i]]) # 맨 앞에는 번호가 들어가게 
        
        file.close()

    def scrap(self) : # 위에서 만든 함수들 사용

        soupPage = self.getHTML(0)
        pages = self.getPages(soupPage)

        file = open('indeed.csv','w', newline='') #프로그램 실행시마다 새로 시작하도록 'w'옵션 넣기
        wr = csv.writer(file)
        wr.writerow(["No.", "Link","Title", "Location"])
        file.close()

        for i in range(pages) : 
            soupCard = self.getHTML(i)
            self.getCards(soupCard, i)
            print(i+1, "번째 페이지 Done")

if __name__ == "__main__":
    s = Scraper()
    s.scrap()
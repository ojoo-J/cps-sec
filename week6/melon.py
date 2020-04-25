from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time


path = os.getcwd() + "/week6/chromedriver.exe"
driver = webdriver.Chrome(path)

try:
    driver.get("https://www.melon.com/index.htm")
    time.sleep(1)

    searchIndex = "사랑" #검색할 내용

    element = driver.find_element_by_xpath('//*[@id="top_search"]') #검색창 찾기
    element.send_keys(searchIndex) #searchIndex를 검색하자!
    driver.find_element_by_class_name("btn_icon.search_m").click() #검색버튼 찾고 클릭
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="divCollection"]/ul/li[3]/a').click()
    
    
    title = []
    for i in range(3): 
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")
        conts = bs.find_all("table")[0].find("tbody").find_all("tr") 

        title.append("\n<<<<page"+str(i+1)+">>>>") #페이지 번호 출력

        for c in conts: # title 따기 반복
            title.append(c.find_all("td", class_ = "t_left")[0].find("a", class_ = "fc_gray").text) # 제목 추출 -> title 리스트에 담기

        driver.find_element_by_xpath('//*[@id="pageObjNavgation"]/div/a[3]').click() #다음버튼 눌러서 페이지 넘기기
    

    
    
finally:
    for t in title:
        print(t)
    driver.quit()

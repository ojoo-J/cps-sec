from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() + "/week6/chromedriver.exe"
driver = webdriver.Chrome(path)


try: 
    driver.get("http://www.kyobobook.co.kr/index.laf?OV_REFFER=https://www.google.com/")
    time.sleep(1)

    searchIndex = "CPS" #검색할 내용
    element = driver.find_element_by_class_name("main_input") #검색창 찾기
    element.send_keys(searchIndex) #searchIndex를 검색하자!
    driver.find_element_by_class_name("btn_search").click() #검색버튼 찾고 클릭

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    pages = int(bs.find("span", id="totalpage").text)
    print(pages)

    title = []
    for i in range(3):
        time.sleep(1)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")
        conts = bs.find("div", class_="list_search_result").find_all("td", class_ = "detail") #앞에 search_list -> 중고 장터는 제외하기 위해서

        title.append("\npage"+str(i+1))
        for c in conts:
            title.append(c.find("div", class_ = "title").find("strong").text) #td(detail)->div(title)->strong의 text만 추출해서 출력

        driver.find_element_by_xpath('//*[@id="contents_section"]/div[9]/div[1]/a[3]').click() #다음버튼 눌러서 페이지 넘기기


finally:
    for t in title:
        print(t)
    driver.quit()

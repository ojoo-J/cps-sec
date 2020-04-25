from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd() #파이썬이 현재 실행중인 경로 (c:\Users\정영주\Desktop\github_test_vscode\practice\cps-sec-1)
path = os.getcwd() + "/week6/chromedriver.exe" #크롬 드라이버가 있는 곳으로 설정

driver = webdriver.Chrome(path)

try:
    driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page1")
    time.sleep(1)

    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")

    #4개의 a태그를 모두 찾은 후 마지막 리스트(마지막 페이지)의 href 반환 = #page21 -> page를 기준으로 split하면 #, 21반환 -> 그 중 인덱스1 반환
    pages = bs.find("div", class_ = "pagination").find_all("a")[-1]["href"].split("page")[1] # =21
    pages = int(pages)
    print(pages)
    
    title = []
    for i in range(pages):
        driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page" + str(i+1))
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("div", class_ = "txtL")
        print("\n<page>" + str(i+1))
        for c in conts:
            print(c.find("a").text)



finally:
    #time.sleep(3)
    driver.quit()



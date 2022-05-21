import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
print("안녕하세요? 당신을 위한 최고의 메뉴를 추천해주는 시스템입니다.")
print("어떤 것을 원하시나요?")
print("ex) 데이트")
print(" 가족")
print(" 친구")
print(" 모임")
print(" 혼자")
n = input()

browser = webdriver.Chrome('C:/Users/a0103/Downloads/chromedriver_win32/chromedriver.exe')

menu = input("특정한 메뉴/코스를 입력해주세요. 없으시다면 엔터키를 눌러주세요.")

region = input("어디에 사시나요?")

try: 
    url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=" + region +" "+menu+ " "+n+"끼리%20"+ "맛집"
    browser.get(url)
    time.sleep(1)
    for _ in range(4):
        browser.find_element_by_css_selector('#poiColl > div.coll_cont.poi_cont > div.wrap_place.wrap_ad').click()
        time.sleep(1)
        
    html = browser.page_source    
    browser.close()

    soup = BeautifulSoup(html, 'html.parser')    
    restaurants = soup.find_all("a", class_="fn_tit")
except:
    try:
        url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q="+region +menu+"%20"+ "맛집"
        browser.get(url)
        time.sleep(1)
        for _ in range(4):
            browser.find_element_by_css_selector('#poiColl > div.coll_cont.poi_cont > div.wrap_place.wrap_ad').click()
            time.sleep(1)
        
        html = browser.page_source    
        browser.close()

        soup = BeautifulSoup(html, 'html.parser')    
        restaurants = soup.find_all("a", class_="fn_tit")
    except:
        print("에러가 발생하였습니다. 더욱 일반적인 검색어를 입력해주시고, 오타가 있는지 확인해주십시오.")

        name = [x.text for x in restaurants]

def trim(string):
    if string[0] == ' ':
        string = string[1:]
    if string[-1] == ' ':
        string = string[:-1]
    return string

name = [trim(x) for x in name]
link = [x['href'] for x in restaurants]
df = pd.DataFrame()
df['name'] = name
df['link'] = link
print(name[0]+"에서 어떠신가요?")
print("상세보기 --> ", link[0])

what = input("다른 것을 원하시나요? y/n")
if(what == "n"):
    print("맛있게 식사하세요.")
else:
    print("전체입니다")
    df = pd.DataFrame()
    df['name'] = name
    df['link'] = link

    print(df)

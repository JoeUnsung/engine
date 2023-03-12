# 작성일: 23-03-11
# 원천: https://www.courtauction.go.kr/
# 크롬 드라이버: https://sites.google.com/a/chromium.org/chromedriver/downloads
# Local path:

import selenium
from selenium import webdriver

from bs4 import BeautifulSoup as bs
import pandas

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains ## Click 실행을 하기 위해 임포트
from selenium.webdriver.common.by import By ## CSS셀렉터로 변환하기 위해 임포트
from webdriver_manager.chrome import ChromeDriverManager



def run():
    print("Start Engine")

    ## 접근 URL 정리
    path_driver = '/Users/joe/github/engine/app/chromedriver_mac64/chromedriver'

    url = 'https://www.courtauction.go.kr/' ## https://를 붙여줘야 에러가 안남
    naver = 'https://www.naver.com/' ## https://를 붙여줘야 에러가 안남

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print("Current session is {}".format(driver.session_id))
    driver.implicitly_wait(10)
    driver.get(url)
    # driver.get(naver)

    driver.switch_to.frame('indexFrame')
    html = driver.page_source
    print(html)

    element = driver.find_element(by=By.CSS_SELECTOR,value="img[alt='경매물건']") # 홈화면 > 경매물건
    actions = ActionChains(driver)
    actions.move_to_element(element).click().perform() ## 버튼 클릭
    driver.implicitly_wait(10)



    print("=============================================")

    document_element = driver.execute_script("return document.documentElement;")
    print(document_element)

    soup = bs(html, 'html.parser')
    # print(soup)

    driver.quit()



if __name__ == '__main__':
    run()


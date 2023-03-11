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
from webdriver_manager.chrome import ChromeDriverManager



def run():
    print("Start Engine")
    # path_driver = '/Users/joe/github/engine/app/chromedriver_mac64_111/chromedriver'
    # path_driver_arm = '/Users/joe/github/engine/app/chromedriver_mac_arm64/chromedriver'

    path_driver = '/Users/joe/github/engine/app/chromedriver_mac64/chromedriver'

    url = 'https://www.courtauction.go.kr/' ## https://를 붙여줘야 에러가 안남
    naver = 'https://www.naver.com/' ## https://를 붙여줘야 에러가 안남

    # options = Options()
    # options.add_argument("start-maximized")
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # driver.get(naver)

    # driver = webdriver.Chrome(executable_path=path_driver)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print("Current session is {}".format(driver.session_id))
    # driver.get(naver)
    driver.implicitly_wait(10)
    driver.get(url)
    # driver.get(naver)

    html = driver.page_source
    soup = bs(html, 'html.parser')

    print(soup)

    # # driver.quit()
    # try:
    #     driver.get(naver)
    # except Exception as e:
    #     print(e.message)




if __name__ == '__main__':
    run()


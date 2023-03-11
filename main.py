# 작성일: 23-03-11
# 원천: https://www.courtauction.go.kr/
# 크롬 드라이버: https://sites.google.com/a/chromium.org/chromedriver/downloads
# Local path:

import selenium
from selenium import webdriver

import bs4
import pandas




def run():
    print("Start Engine")

    path_driver = '/Users/joe/github/engine/app/chromedriver_mac64/chromedriver'
    path_driver_arm = '/Users/joe/github/engine/app/chromedriver_mac_arm64/chromedriver'

    driver = webdriver.Chrome(path_driver)
    driver.implicitly_wait(3)

    driver.get('https://google.com')



if __name__ == '__main__':
    run()


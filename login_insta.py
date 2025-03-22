# seleniumの設定
# from seleniumwire import webdriver  # Import from seleniumwire
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException,ElementClickInterceptedException,StaleElementReferenceException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.support.select import Select
import math
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import sys
import json
import re
import os
from collections import Counter
from csv import writer
import csv
import random
import threading
import logging
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
#ランダム数の作成
randomC = random.uniform(10,15)


##chormeのオプションを指定
options = webdriver.ChromeOptions()
# options.add_argument("--headless")# ヘッドレスで起動するオプションを指定
options.page_load_strategy = 'normal'
# options.page_load_strategy = 'eager'
# options.add_argument(ua.random)
driver = webdriver.Chrome(options=options)

# options.add_argument("--incognito")
# options.add_argument("--no-startup-window")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1200,1200")
# options.add_argument("--no-sandbox")
# options.add_argument("--enable-javascript")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument("--enable-webgl")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument('--disable-dev-shm-usage')#ディスクのメモリスペースを使う。DockerやGcloudのメモリ対策でよく使われる。
# options.add_argument('blink-settings=imagesEnabled=false')  # 画像の読み込みを無効化
# options.add_argument('--disable-cache')


path = os.getcwd()
CHROMEDRIVER = path + r'\chromedriver.exe'



url = "https://www.instagram.com/"




driver.get(url)  # Cookieを設定したいWebサイトにアクセス

# CookieをJSONファイルから読み込む
with open("cookies.json", "r") as f:
    cookies = json.load(f)

# Cookieを設定
for cookie in cookies:
    driver.add_cookie(cookie)

driver.get(url)  # Cookieが設定された状態でWebサイトにアクセス
time.sleep(10)

#click follower
follower = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/h3/div[2]/strong')
follower.click()
time.sleep(10)


#mouse over 
# マウスオーバーしたい要素を取得
scrollable_element = driver.find_element(By.CLASS_NAME, "css-wq5jjc-DivUserListContainer")  # 例: 要素のID

# マウスオーバー
# actions = ActionChains(driver)
# actions.move_to_element(scrollable_element).perform()

# スクロール量（ピクセル数）
scroll_amount = 3000

# JavaScriptで要素内のスクロールを実行
acount_list = []
for _ in range(300): #5回スクロールする。
    print(f"number{_}")
    try:
        driver.execute_script(f"arguments[0].scrollTop += {scroll_amount};", scrollable_element)
        # acounts = driver.find_elements(By.CLASS_NAME,'e1bph0nm2.css-7mf1fq-Button-StyledFollowButtonV2.ehk74z00')
        # acounts = driver.find_elements(By.XPATH,'//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[*]/div/div/a/div/p')

        # for param in acounts:
        #     acount = param.text
        #     print(acount)
        #     acount_list.append(acount)
        # acount_list = list(set(acount_list))
        # print(len(acount_list))
        # print(acount_list)
#accountIDの取得
        
    except WebDriverException as e:
        print(f"WebDriverエラーが発生しました: {e}")
        break
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")    
        break
    time.sleep(1) #スクロール後の読み込み待ち。


acounts = driver.find_elements(By.XPATH,'//*[@id="tux-portal-container"]/div/div[2]/div/div/div[2]/div/div/section/div/div[3]/li[*]/div/div/a/div/p')

for param in acounts:
    acount = param.text
    # print(acount)
    acount_list.append(acount)
acount_list = list(set(acount_list))
print(len(acount_list))
# print(acount_list)

df = pd.DataFrame(acount_list)
html_source = driver.page_source
with open("source.html",mode = "w",encoding ='utf-8') as f:
    f.write(html_source)
df.to_csv('follwers.csv',mode = 'w',encoding='utf-8',index=False,header=None)

driver.quit()

# dyqtimf4ye58 check acount
    





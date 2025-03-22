# seleniumの設定

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

# time.sleep(randomC)
# options.add_argument(ua.random)
# すべてのCookieを削除
driver.implicitly_wait(10)


"""
進め方　cookieを取得
cookieを使ってwebサイトにアクセス⇒ログイン状態をたもっているか確認。

followerをクリックした後のHTMLを取得。
アカウント名がどこにあるか？確認する。⇒geminiに解析してもらう。
"""



driver.get(url)
#click follower
time.sleep(20)

# follower = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/h3/div[2]/strong')
# follower.click()

# time.sleep(20)
# try:
#     step1 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div[2]/div/div')
#     print("pattern1")
# except:
#     step1 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div')
#     print("pattern2")


# step1.click()
# step2 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div[2]/div[2]/div')
# step2.click()

# step3 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/form/div[1]/a')
# step3.click()

# #mail input 
# mail_input  = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/input')
# mail_input.send_keys('mememori8888@gmail.com')
# #password input
# password_input  = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input')
# password_input.send_keys('Mm19830831!')
# #login click
# login_click  = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/button')
# login_click.click()
#パズルに認証の為、ここで待機
time.sleep(200)
#get cookie
cookies = driver.get_cookies()

# CookieをJSON形式でファイルに保存
import json

with open("cookies.json", "w") as f:
    json.dump(cookies, f)

print("cookie更新")
#click follower
# follower = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/h3/div[2]/strong')
# follower.click()

#login処理
time.sleep(60)
# ページのソースコードを取得
html_source = driver.page_source
with open("source.html","w",encoding ='utf-8') as f:
    f.write(html_source)

driver.quit()
# # BeautifulSoupで解析
# soup = BeautifulSoup(html_source, 'html.parser')

# # インデントして整形
# # aria-label属性を持つdiv要素を検索
# div_elements = soup.find_all('div', {'aria-label': True})

# for div in div_elements:
#     store_name = div.get('aria-label')
#     # print(store_name) 
#     store_names = [area_select_text,city_select_text,store_name]
#     # 既存のCSVファイルに追記
#     df = pd.DataFrame([store_names])
#     print(df)
#     df.to_csv("output.csv",mode = 'a',index=False,header=None,encoding='utf-8')

# from selenium import webdriver

# driver = webdriver.Chrome()  # または他のWebDriver

# driver.get("https://www.example.com")  # Cookieを取得したいWebサイトにアクセス

# cookies = driver.get_cookies()

# # CookieをJSON形式でファイルに保存
# import json

# with open("cookies.json", "w") as f:
#     json.dump(cookies, f)

# driver.quit()

# from selenium import webdriver
# import json

# driver = webdriver.Chrome()  # または他のWebDriver

# driver.get("https://www.example.com")  # Cookieを設定したいWebサイトにアクセス

# # CookieをJSONファイルから読み込む
# with open("cookies.json", "r") as f:
#     cookies = json.load(f)

# # Cookieを設定
# for cookie in cookies:
#     driver.add_cookie(cookie)

# driver.get("https://www.example.com")  # Cookieが設定された状態でWebサイトにアクセス

# driver.quit()


    






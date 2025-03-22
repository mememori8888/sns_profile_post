

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



urls = ["https://www.tiktok.com/@yuj_224",
"https://www.tiktok.com/@wnsgml9054",
"https://www.tiktok.com/@okdick",
"https://www.tiktok.com/@sukidayo.7",
"https://www.tiktok.com/@johan_05_7",
"https://www.tiktok.com/@user703568430",
"https://www.tiktok.com/@user4967362508153",
"https://www.tiktok.com/@user80331582783832",
"https://www.tiktok.com/@kao111314",
"https://www.tiktok.com/@user483764106",
"https://www.tiktok.com/@hqy3030ysq",

]
# time.sleep(randomC)
# options.add_argument(ua.random)
# すべてのCookieを削除
# driver.implicitly_wait(10)


# """
# 進め方　cookieを取得
# cookieを使ってwebサイトにアクセス⇒ログイン状態をたもっているか確認。

# followerをクリックした後のHTMLを取得。
# アカウント名がどこにあるか？確認する。⇒geminiに解析してもらう。
# """



# driver.get(url)
# #click follower
# time.sleep(20)

# # follower = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/h3/div[2]/strong')
# # follower.click()

# # time.sleep(20)
# # try:
# #     step1 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div[2]/div/div')
# #     print("pattern1")
# # except:
# #     step1 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div')
# #     print("pattern2")


# # step1.click()
# # step2 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div[2]/div[2]/div')
# # step2.click()

# # step3 = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div/form/div[1]/a')
# # step3.click()

# # #mail input 
# # mail_input  = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/input')
# # mail_input.send_keys('mememori8888@gmail.com')
# # #password input
# # password_input  = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/div[2]/div/input')
# # password_input.send_keys('Mm19830831!')
# # #login click
# # login_click  = driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/div/div[1]/div[1]/div[2]/form/button')
# # login_click.click()
# #パズルに認証の為、ここで待機
# time.sleep(200)
# #get cookie
# cookies = driver.get_cookies()

# # CookieをJSON形式でファイルに保存
# import json

# with open("cookies.json", "w") as f:
#     json.dump(cookies, f)
# #click follower
# # follower = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/h3/div[2]/strong')
# # follower.click()

# #login処理
# time.sleep(200)
# # ページのソースコードを取得
# html_source = driver.page_source
# with open("source.html","w",encoding ='utf-8') as f:
#     f.write(html_source)

# driver.quit()
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


for url in urls:
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
    # html_source = driver.page_source
    # with open("source.html",mode = "w",encoding ='utf-8') as f:
    #     f.write(html_source)
    df.to_csv('follwers.csv',mode = 'a',encoding='utf-8',index=False,header=None)

driver.quit()

# dyqtimf4ye58 check acount
    





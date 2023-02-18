from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import bs4
import random
import chromedriver_binary

import secret


# 現在の時刻を表す
def now_time():
    dt_now = datetime.datetime.now()
    return dt_now.strftime('%m/%d %H:%M')+' '


# インスタログイン情報
USERNAME = secret.username
PASSWORD = secret.password

# 検索するハッシュタグ
tagName = random.choice(['midjourney', 'aiart', 'aiartwork'])
print(tagName)

# いいね数
likedMax = 50

# GoogleChrome自動操作準備

# GoogleChromeサイト開く
driver = webdriver.Chrome(ChromeDriverManager().install())
# インスタサイトを開く
driver.get('https://www.instagram.com/')
print(now_time()+'instagramにアクセスしました')
time.sleep(2)

# ユーザーネームパスワード入力
driver.find_element_by_name('username').send_keys(USERNAME)
time.sleep(2)
driver.find_element_by_name('password').send_keys(PASSWORD)
time.sleep(2)

# ログインボタン押下
btns = driver.find_elements_by_tag_name("button")
for i in btns:
    if i.text == 'ログイン' or i.text == 'Log in':
        i.click()
        break
time.sleep(2)
print(now_time()+'instagramにログインしました')
time.sleep(5)

# ハッシュタグ検索
instaurl = 'https://www.instagram.com/explore/tags/'
driver.get(instaurl + tagName)
time.sleep(5)
print(now_time()+'#検索を行いました')
time.sleep(5)

# 直近で投稿されたページに移動
target = driver.find_element_by_class_name('_aagu')
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
print(now_time()+'最新の投稿まで移動しました')
time.sleep(5)

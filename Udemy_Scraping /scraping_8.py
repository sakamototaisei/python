"""
Seleniumでログインする方法
"""
from click import password_option
from selenium import webdriver
from time import sleep


NUMBER = '09080886767'
PASSWORD = 'taisei040389'

driver = webdriver.Chrome("/Users/sakamototaisei/Desktop/python/Udemy_Scraping /chromedriver")
target_url = 'https://www.instagram.com/'
# インスタのログイン画面へ遷移
driver.get(target_url)
sleep(3)

# ユーザーネームとパスワード入力欄の取得
error_fig = False

try:
    # ユーザーネーム欄に記述
    username_input = driver.find_element_by_xpath('//input[@aria-label="電話番号、ユーザーネーム、メールアドレス"]')
    username_input.send_keys(NUMBER)
    sleep(1)
    # パスワード欄の記述
    password_input = driver.find_element_by_xpath('//input[@aria-label="パスワード"]')
    password_input.send_keys(PASSWORD)
    sleep(1)

    # ログインボタンを押す
    login_button = driver.find_element_by_xpath('//button[@type="submit"]')
    login_button.submit()
    sleep(1)

except Exception:
    error_fig = True
    print('ユーザー名、パスワード入力時にエラーが発生しました。')

# エラーフラグの確認
if error_fig is False:
    try:
        sleep(1)
        notnow_button = driver.find_element_by_xpath('//button[text()="後で"]')
        # 要素のクリック
        notnow_button.click()
        sleep(1)

        # 通知画面を消す
        notice_button = driver.find_element_by_xpath('//button[text()="後で"]')
        # 要素のクリック
        notice_button.click()
        sleep(1)
    except Exception:
        pass
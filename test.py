from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# ブラウザを立ち上げインスタンス化する
browser = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://scraping-for-beginner.herokuapp.com/login_page'

browser.get(url)
from selenium import webdriver
import chromedriver_binary

#https://hacknote.jp/archives/48685/
#https://developers.google.com/web/updates/2017/04/headless-chrome?hl=ja

#---headON mode---------
driver = webdriver.Chrome()

# Google検索画面にアクセス
driver.get('https://www.google.co.jp/')

# 検索エリア取得、ホゲホゲとか入れて。。。
searchInput = driver.find_element_by_name("q")
searchInput.send_keys("hogehoge")

# 検索（ただしサジェスト入るので５秒くらい待たせてます
driver.implicitly_wait(5)
driver.find_element_by_name("btnK").click()

# 終了処理
driver.quit()
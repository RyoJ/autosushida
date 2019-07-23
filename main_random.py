#main.py

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#Chrome Driverのパス
driver_path = './chromedriver.exe'
#ドライバーを開く
driver = webdriver.Chrome(driver_path)

#ウインドウサイズを固定
#+123としているのは、「Chromeは自動テストソフトウェアによって制御されています。」という部分を考慮している
windows = (500,420+123)
driver.set_window_size(*windows)

# OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)

#寿司打のゲーム画面をずらすために書く
target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)
actions = ActionChains(driver)
actions.move_to_element(webgl_element).perform()

#クリックする前にロード時間待機
sleep(10)

#スタートボタンの座標
center_x = 250
center_y = 256

#スタートボタンをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()

print("スタートボタンをクリックしました。")

#ボタンが表示されるまで待つ
sleep(2)

#お勧めのコースをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()

print("お勧めコースのボタンをクリックしました。")

#<body>に向かってキーを入力させる
target_xpath = '/html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

#時計を計測
from time import time
start = time()

while time() - start < 90.0:
#文字をテキトーに入力
    element.send_keys("abcdefghijklmnopqrstuvwxyz-!?.,")
    
input("何か入力してください")

#ドライバーを閉じる
driver.close()
driver.quit()
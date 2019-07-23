#main.py

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pyocr
import pyocr.builders

#Chrome Driverのパス
driver_path = './chromedriver.exe'
#ドライバーを開く
driver = webdriver.Chrome(driver_path)

#ウインドウサイズは全画面

# OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)

target_xpath = '//*[@id="game"]/div'#"game"という値を持つタグの最初のdiv要素 #要素を見つける"https://kurozumi.github.io/selenium-python/locating-elements.html"
webgl_element = driver.find_element_by_xpath(target_xpath)#targetを見つける。この場合webgl_element
actions = ActionChains(driver)#ActionChainを使えるようにする
#actions.move_to_element(webgl_element).perform()#寿司打のゲーム画面は全画面のためずらさない

#クリックする前にロード時間待機
time.sleep(20)

#スタートボタンの座標
center_x = 250
center_y = 250

#スタートボタンをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()

print("スタートボタンをクリックしました。")

#ボタンが表示されるまで待つ
time.sleep(2)

#お勧めのコースをクリックする
actions = ActionChains(driver)
actions.move_to_element_with_offset(webgl_element, center_x, center_y).click().perform()

print("お勧めコースのボタンをクリックしました。")

#<body>に向かってキーを入力させる
target_xpath = '/html/body'
element = driver.find_element_by_xpath(target_xpath)
element.send_keys(" ")

# 時間を計測
from time import time
start = time()

while time() - start < 90.0:
    element.send_keys("abcdefghijklmnopqrstuvwxyz-!?.,")


input("何か入力してください")

#ドライバーを閉じる
driver.close()
driver.quit()
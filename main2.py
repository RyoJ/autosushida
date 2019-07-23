# main.py

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Chrome Driverのパス
driver_path = './chromedriver.exe'
# ドライバーを開く
driver = webdriver.Chrome(driver_path)

# ウィンドウサイズを固定
# +123としているのは、
# 「Chromeは自動テストソフトウェアによって制御されています。」
# という部分を考慮している
window = (500, 420+123)
driver.set_window_size(*window)

# OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)

# 寿司打のゲーム画面をずらすために書く
target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)
actions = ActionChains(driver)
actions.move_to_element(webgl_element)
actions.perform()

input("何か入力してください")

# ドライバーを閉じる
driver.close()
driver.quit()
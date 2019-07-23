from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import Image
import pyocr
import pyocr.builders
import sys 

# Chrome Driverのパス
driver_path = '../chromedriver.exe'
# ドライバーを開く
driver = webdriver.Chrome(driver_path)
# OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)
#しばらく次の処理を待つ
time.sleep(10)
#スタートボタンの座標
center_x = 260
center_y = 250
#スタートボタンをクリックする(ref:https://qiita.com/mochio/items/dc9935ee607895420186)
target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)
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

# 画像の範囲を指定するためのリスト
im_ranges = [136, 124, 112, 100, 88, 76]#よくわからん

# PyOCRのツール
tools =  pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]

# 時間を計測
from time import time
start = time()

while time() - start < 250.0:
        
    # ファイル名
    fname = "sample_image.png"
    # スクショをする
    driver.save_screenshot(fname)

    # 画像をPILのImageを使って読み込む
    # ローマ字の部分を取り出す
    im = Image.open(fname).crop((500,450,750,480))


    # 画像がちゃんと切り取られているかの確認
    im.save("sample.png")

    # tool で文字を認識させる
    text = tool.image_to_string(im, lang='eng', builder=pyocr.builders.TextBuilder())

    # text を確認
    print(text)

    # 文字を入力させる
    element.send_keys(text)

#press anykeyで閉じるようにする
input("何か入力してください")
#ドライバーを閉じる
driver.close()
driver.quit()
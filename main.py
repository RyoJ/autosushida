#main.py

from time import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import pyocr
import pyocr.builders

#Chrome Driverのパス
driver_path = './chromedriver.exe'
#ドライバーを開く
driver = webdriver.Chrome(driver_path)

#ウインドウサイズを固定
#+123としているのは、「Chromeは自動テストソフトウェアによって制御されています。」という部分を考慮している
windows = (500,420+123)
driver.set_window_size(*window)

# OpenGL版の寿司打を開く
target_url = 'http://typingx0.net/sushida/play.html'
driver.get(target_url)

#寿司打のゲーム画面をずらすために書く
target_xpath = '//*[@id="game"]/div'#"game"という値を持つタグの最初のdiv要素 #要素を見つける"https://kurozumi.github.io/selenium-python/locating-elements.html"
webgl_element = driver.find_element_by_xpath(target_xpath)#targetを見つける。この場合webgl_element
actions = ActionChains(driver)#ActionChainを使えるようにする
actions.move_to_element(webgl_element).perform()#マウスをwebgl要素の中央に移動してホールドする

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

#画像の範囲を指定するためのリスト
im_ranges = [136, 124, 112, 100, 88, 76]

#PyOCRのツール
tool = pyocr.get_available_tools()[0]

#時計を計測
from time import time
start = time()
while time() - start < 90.0:

    #移動した
    #ファイル名
    fname = "sample_image.png"
    #スクショをする
    driver.save_screenshot(fname)

    #画像をPILのImagesを使って読み込む
    #ローマ字の部分を取り出す
    im = Image.open(fname).crop((0,230,500,254))

    #画像の範囲を指定する
    for im_range in im_ranges:
        if im.getpixel((im_range, 0)) == (255, 255, 255, 255):
            im = im.crop((im_range+20, 0, 500-im_range-20, 24))

            #画像を二値化する
            im = im.convert("L")
            for i in range(im.size[0]):
                for j in range(im.size[1]):
                    if im.getpixel((i,j)) >= 128:
                        im.putpixel((i,j),0)
                    else:
                        im.putpixel((i,j),255)
            break

    #画像がちゃんと切り取られているかの確認
    im.save("sample.png")

    #toolで文字を認識させる
    text = tool.image_to_string(im, lang='eng', builder=pyocr.builders.TextBuilder())

    #textを認識
    print(text)

    #文字を入力させる
    element.send_keys(text)

"""

!!この部分は消す!!
#文字をテキトーに入力
    element.send_keys("abcdefghijklmnopqrstuvwxyz-!?.,")

"""

input("何か入力してください")

#ドライバーを閉じる
driver.close()
driver.quit()
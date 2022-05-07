from bs4 import BeautifulSoup
from selenium import webdriver



try:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") #讓瀏覽器 不用跳出視窗 背景運作
    chrome  = webdriver.Chrome(options=options, executable_path = 'C:/Users/heart/Desktop/project/pttbug/chromedriver')  #建立物件進行初始化
    chrome.set_page_load_timeout(10)  #這次自動化測試 讓動作延遲
    chrome.get('https://code-gym.github.io/spider_demo/')
    soup = BeautifulSoup(chrome.page_source, 'html5lib') #解析網頁資訊並回傳
    print(soup.find('h1').text)




finally:
    chrome.quit()
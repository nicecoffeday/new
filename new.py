from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') #讓瀏覽器 不用跳出視窗 背景運作
    chrome  = webdriver.Chrome(executable_path = 'C:/Users/heart/Desktop/project/pttbug/chromedriver')  #建立物件進行初始化
    chrome.set_page_load_timeout(10)  #這次自動化測試 讓動作延遲
    chrome.get('https://code-gym.github.io/spider_demo/')
    soup = BeautifulSoup(chrome.page_source, 'html5lib') #解析網頁資訊並回傳
    print(soup.find('h1').text)

    chrome.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/div/div/h3/a').click()  #點擊標題
    print(chrome.find_element(By.XPATH, '//*[@id="post-header"]/div[2]/div/div/h1').text)   # 抓取需要的文字




finally:
    chrome.quit()
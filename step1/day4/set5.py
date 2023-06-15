# pip install selenium
# pip install chromedriver_autoinstaller // 크롬 드라이버를 다운하지 않아도 자동을 잡아주는 툴
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'https://www.hanatour.com/'
driver.get(url)
time.sleep(1)
try:
    cnt = 5
    pagedown=1
    body = driver.find_element(By.TAG_NAME,'body')
    while pagedown < cnt:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        pagedown += 1
    soup =BeautifulSoup(driver.page_source,'html.parser')
    print(soup.prettify())
except Exception as e:
    print(str(e))

driver.quit() # 종료
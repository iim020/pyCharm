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
url = 'https://www.starbucks.co.kr/store/store_map.do'
driver.get(url)
time.sleep(1)
lis = driver.find_element(By.CSS_SELECTOR,'loac_search').click()
time.sleep(1)
lis = driver.find_element(By.CSS_SELECTOR,'#tCSB_2_container > ul > li:ntn-child(1)')
total = len(lis)
print('매장 수 :', total)
time.sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')
lis = driver.find_elements(By.CSS_SELECTOR,'#mCSB_3_container > ul > li')

for shop in lis:
    print(shop)
    lat = shop.get_attribute('data_lat')
    long = shop.get('data-long')
    shopnm = shop.select_one('strong').getText()
    shopinfo = shop.select_one('.result_details').getText()
    info = shopinfo.split('<br>')
    print(lat,long,shopinfo)


driver.quit() # 종료
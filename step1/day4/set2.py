# pip install selenium
# pip install chromedriver_autoinstaller // 크롬 드라이버를 다운하지 않아도 자동을 잡아주는 툴
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'https://www.melon.com/chart/index.htm'
driver.get(url)
time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html-parser')
div = soup.select_one('#tb_list')
trs = div.find_all('tr')

# div = driver.find_element(By.ID,'tb_list')
# trs = div.find_elements(By.TAG_NAME,'tr')

for i,tr in enumerate(trs):
    # print(tr.getText())
    print(i,'등 : ',tr.find_all('td')[5].select_one('a').getText())
print('='*100)
driver.quit() # 종료
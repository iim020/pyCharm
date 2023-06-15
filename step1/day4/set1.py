# pip install selenium
# pip install chromedriver_autoinstaller // 크롬 드라이버를 다운하지 않아도 자동을 잡아주는 툴
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'https://www.hanatour.com/'
driver.get(url)


time.sleep(1)
driver.find_element(By.ID, 'input_keyword').send_keys('하와이')
driver.find_element(By.CSS_SELECTOR,'button.btn_search').click()
time.sleep(3)

driver.quit() # 종료
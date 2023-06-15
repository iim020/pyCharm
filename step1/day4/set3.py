# pip install selenium
# pip install chromedriver_autoinstaller // 크롬 드라이버를 다운하지 않아도 자동을 잡아주는 툴
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--user-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url = 'http://192.168.1.54:5500/day1/test.html'
driver.get(url)

alert = Alert(driver) #alert찾이 나타날때까지 대기
print(alert.text)
alert.accept() # 확인버튼
# 만약 confirm일 경우 취소는 dismiss()
div = driver.find_element(By.ID,'div_id')
lis = div.find_element(By.TAG_NAME,'li')

for li in lis:
    print(li.text)
driver.quit() # 종료
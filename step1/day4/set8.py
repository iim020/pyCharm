import time

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromedriver_autoinstaller.install()
UA ='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
options = Options()
options.add_argument(f'--User-agent={UA}')
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3) # 대기
url ='https://www.msn.com/ko-kr/autos?ocid=hpmsn'
driver.get(url)
time.sleep(3)
import util
util.fullpage_screenshot(driver, 'msn.png')
driver.close()

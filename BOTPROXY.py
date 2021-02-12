import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PROXY = 'IP:PORTA'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--proxy-server={PROXY}')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('LINK A SER EXECUTADO')
time.sleep(100)
from selenium import webdriver
import time

page = "https://www.bestbuy.com/site/beats-by-dr-dre-beats-studio-buds-totally-wireless-noise-cancelling-earphones-beats-red/4900921.p?skuId=4900921"

PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH)
driver.implicitly_wait(10)
driver.get(page)

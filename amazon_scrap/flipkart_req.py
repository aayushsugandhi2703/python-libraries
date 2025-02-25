from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url  = 'https://www.flipkart.com/apple-macbook-air-m3-8-gb-512-gb-ssd-macos-sonoma-mryv3hn-a/p/itmb1aa0cc739560?pid=COMGYP5GR35KCWP7&lid=LSTCOMGYP5GR35KCWP78NQPMR&marketplace=FLIPKART&q=macbook%20m3&sattr[]=color&sattr[]=system_memory&sattr[]=ssd_capacity&sattr[]=screen_size&st=color&otracker=search'
driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Nx9bqj.CxhGGd')))
for element in elements:
    print(element.text)
driver.quit()


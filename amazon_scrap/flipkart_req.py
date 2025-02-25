from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, json

url  = 'https://www.flipkart.com/apple-macbook-air-m3-8-gb-512-gb-ssd-macos-sonoma-mryv3hn-a/p/itmb1aa0cc739560?pid=COMGYP5GR35KCWP7&lid=LSTCOMGYP5GR35KCWP78NQPMR&marketplace=FLIPKART&q=macbook%20m3&sattr[]=color&sattr[]=system_memory&sattr[]=ssd_capacity&sattr[]=screen_size&st=color&otracker=search'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)

product_name = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._6EBuvT')))
product_price = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Nx9bqj.CxhGGd')))
product_rating = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._5OesEi.HDvrBb')))
product_reviews = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ipqd2A')))

data = {
    'product_name': product_name,
    'product_price': product_price,
    'product_rating': product_rating,
    'product_reviews': product_reviews,
}

print(json.dumps(data, indent=4))

driver.quit()


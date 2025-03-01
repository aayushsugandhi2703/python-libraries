from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os, json
from email.message import EmailMessage
import smtplib, ssl



url  = 'https://www.flipkart.com/apple-macbook-air-m3-8-gb-512-gb-ssd-macos-sonoma-mryv3hn-a/p/itmb1aa0cc739560?pid=COMGYP5GR35KCWP7&lid=LSTCOMGYP5GR35KCWP78NQPMR&marketplace=FLIPKART&q=macbook%20m3&sattr[]=color&sattr[]=system_memory&sattr[]=ssd_capacity&sattr[]=screen_size&st=color&otracker=search'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)

product_name = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._6EBuvT')))
product_price = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.Nx9bqj.CxhGGd')))
product_rating = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._5OesEi.HDvrBb')))
product_reviews = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ipqd2A')))

data = {
    'product_name': product_name[0].text,
    'product_price': product_price[0].text,
    'product_rating': product_rating[0].text,
    'product_reviews': product_reviews[0].text,
}

details =json.dumps(data, indent=4)
print(details)
# Sending the email notifications

sender_email = "aayush.sugandhi@gmail.com"
receiver_email = "eng22cs0218@dsu.edu.in"
password = "password"
subject = "Flipkart Product Details"
body = """
this is just a notification email for testing for first time
"""
# adding the data to the email
em = EmailMessage()
em['from'] = sender_email
em['to'] = receiver_email
em['subject'] = subject
em.set_content(body + details )

# for securing the email
context = ssl.create_default_context()

# sending the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, em.as_string())


driver.quit()


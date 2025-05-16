from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")

time.sleep(5)

username = driver.find_element(By.NAME, 'username')
username.send_keys("pvt._.boy")

password = driver.find_element(By.NAME, 'password')
password.send_keys("T23EJICS054")

login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div/button')
login_button.click()

time.sleep(10)

driver.quit()
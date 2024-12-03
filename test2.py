from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = Options()
service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://userinyerface.com/game.html")
element1 = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]')
print(element1.value_of_css_property("width") == "300px")
print(element1.value_of_css_property("height") == "175px")
# driver.get("https://www.youtube.com/")
# search=driver.find_element()
time.sleep(5)
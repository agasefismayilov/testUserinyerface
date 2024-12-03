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
print(element1.value_of_css_property("background-color") == "rgba(255, 0, 0, 1)")
print(element1.value_of_css_property("height") == "155.2px")
# driver.get("https://www.youtube.com/")
# search=driver.find_element()
time.sleep(5)
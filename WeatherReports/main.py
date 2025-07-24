import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep, time
import datetime as dt

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.accuweather.com/')

sleep(2)

cookie_consent = driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button[2]/p")
cookie_consent.click()

sleep(1)
location = 'Illoqqortoormiut, GL'

search_field = driver.find_element(By.NAME, value="query")
search_field.send_keys(location)
search_field.send_keys(Keys.RETURN)

sleep(2)

details = driver.find_element(By.CLASS_NAME, value='forecast-container')
details.click()
sleep(1)

conditions = driver.find_element(By.CLASS_NAME, value='phrase').text
temperature = driver.find_element(By.CLASS_NAME, value='display-temp').text
humidity = driver.find_element(By.XPATH, value='/html/body/div/div[7]/div[1]/div[1]/div[2]/div[3]/div[6]/div[2]').text
wind = driver.find_element(By.XPATH, value='/html/body/div/div[7]/div[1]/div[1]/div[2]/div[3]/div[4]/div[2]').text
cloud_cover = driver.find_element(By.XPATH, value="/html/body/div/div[7]/div[1]/div[1]/div[2]/div[3]/div[10]/div[2]").text
visibility = driver.find_element(By.XPATH , value="/html/body/div/div[7]/div[1]/div[1]/div[2]/div[3]/div[11]/div[2]").text
cloud_ceiling = driver.find_element(By.XPATH, value="/html/body/div/div[7]/div[1]/div[1]/div[2]/div[3]/div[12]/div[2]").text
now = dt.datetime.now()
current_time = now.strftime('%Y-%m-%d %H:%M:%S')
data = {
    'location': location,
    'conditions': conditions,
    'temperature': temperature,
    'humidity': humidity,
    'wind': wind,
    'cloudCover': cloud_cover,
    'visibility': visibility,
    'cloudCeiling': cloud_ceiling,
    'timestamp': current_time,
}

print(data)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np
data = []
driver = webdriver.Chrome("C:/Users/A/Desktop/chromedriver.exe")

# 산데이터
mt_csv = pd.read_csv("C:/Users/A/Downloads/santa.csv", encoding='cp949')
mt = pd.DataFrame.to_numpy(mt_csv)

url = "https://www.google.co.kr/maps/?hl=ko"

driver.get(url)

time.sleep(1.5)

for i in range(4702):
    element = driver.find_element(By.NAME, "q")
    element.clear()
    element.send_keys(mt[i][0])

    driver.find_element(By.ID, "searchbox-searchbutton").click()

    time.sleep(3.5)

    location_url = driver.current_url

    # LAT
    index = location_url.find("!8m2!3d")
    location_url = location_url[index + 7:]

    # LON
    index2 = location_url.find("!4d")

    print("LAT = " + location_url[:index2] + "LON = " + location_url[index2 + 3:-6])
    print(driver.current_url)

    ## 엑셀로담기
    data.append([mt[i][0], location_url[:index2], location_url[index2 + 3:-6]])

dt_frame = pd.DataFrame(data)
dt_frame.to_csv("C:/Users/A/Desktop/res.csv",header=False, index=False)

# 규칙 !8m2!3d 이후 LAT !4d 이후 LON
from selenium import webdriver
from datetime import datetime, timedelta
import time

chrome_driver = '/Users/mukulperiwal/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get('https://orteil.dashnet.org/cookieclicker/')

game_time = datetime.now()
stop_time = str(datetime.now() + timedelta(seconds=30))[:19]

cookie = driver.find_element_by_id('bigCookie')
count = 0
while True:
    cookie.click()
    if stop_time == str(datetime.now())[:19] and count == 0:
        cookies_per_sec = driver.find_element_by_css_selector("#cookies").text
        print(cookies_per_sec[cookies_per_sec.index(':')+2:])
        count += 1

    if str(datetime.now())[:19] == str(game_time + timedelta(seconds=5))[:19]:
        try:
            click_button = driver.find_element_by_css_selector(
                ".cc_banner-wrapper a.cc_btn")
        except:
            pass
        else:
            click_button.click()
        finally:
            products = driver.find_elements_by_css_selector("#products div.enabled")
            prices = []
            for i in range(len(products)):
                prices.append(float(driver.find_element_by_id(f"productPrice{i}").text.replace(",", "")))
            max_price = max(prices)
            products[prices.index(max_price)].click()
            game_time = datetime.now()

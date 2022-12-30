from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument(r'--user-data-dir=C:\Users\91892\AppData\Local\Google\Chrome\User Data\Default')
chrome_options.add_argument('--profile-directory-Default')

driver = webdriver.Chrome("chromedriver", options=chrome_options)
driver.get("https://amazon.com")

driver.find_element("xpath", "//input[@class='nav-input nav-progressive-attribute']").send_keys("keyboard \n")

time.sleep(1)

product = driver.find_element("xpath", '//img[@src="https://m.media-amazon.com/images/I/81dLH5W903L._AC_UY218_.jpg"]')

product.click()

buy_now = driver.find_element("xpath", '//input[@id="buy-now-button"]')
buy_now.click()

# Entering phone number
driver.find_element("xpath", "//input[@id='ap_email']").send_keys("12345678990")


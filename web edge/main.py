from asyncio.windows_events import NULL
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from time import sleep

# browser = webdriver.Edge()

def do_searches(searches, driver):
    for i in range(searches):
        driver.switch_to.new_window('tab')
        driver.get("https://")
        print("Done {i}")

edge_options = Options()

driver = webdriver.Edge(options = edge_options)

driver.maximize_window()

driver.switch_to.new_window('tab')

driver.get("https://login.live.com")

# sleep(15)

# check = driver.find_element("xpath", '//*[@class="_2Evhc1Nj0AOSMKq6j11gui"]')
# check.click()

# sleep(1)

# check = driver.find_element("xpath", '//*[@id="mectrl_body_signOut"]')
# check.click()

# sleep(5)

# driver.get("https://login.live.com")

# sleep(2)

# check = driver.find_element("xpath", '//input[@class="form-control ltr_override input ext-input text-box ext-text-box"]')
# check.send_keys("omgarg8700@outlook.com")

# check = driver.find_element("xpath", '//input[@class="win-button button_primary button ext-button primary ext-primary"]')
# check.click()

# sleep(2)

# check = driver.find_element("xpath", '//input[@class="form-control input ext-input text-box ext-text-box"]')
# check.send_keys("4Zn&Wf1[")

# check = driver.find_element("xpath", '//input[@class="win-button button_primary button ext-button primary ext-primary"]')
# check.click()

# sleep(5)

# print("YAY We have done it")

# do_searches(30, driver)

driver.get("https://rewards.bing.com")
driver.close()
driver.quit()





# System.setProperty("webdriver.edge.driver", "your\\path\\to\\edge\\webdriver\\msedgedriver.exe"); 
# EdgeOptions edgeOptions = new EdgeOptions();

# // Here you set the path of the profile ending with User Data not the profile folder
# edgeOptions.addArguments("user-data-dir=C:\\Users\\username\\AppData\\Local\\Microsoft\\Edge\\User Data");

# // Here you specify the actual profile folder
# edgeOptions.addArguments("profile-directory=Profile 2");

# edgeOptions.addArguments("--start-maximized");
# WebDriver driver = new EdgeDriver(edgeOptions); 
# driver.get("https://www.google.com");


# class="_2Evhc1Nj0AOSMKq6j11gui"
# class="_2Evhc1Nj0AOSMKq6j11gui"

# <button id="mectrl_main_trigger" type="button" class="mectrl_resetStyle mectrl_trigger" aria-label="Account manager for OM" aria-expanded="false" aria-controls="mectrl_main_body" data-noclose="true">

# form-control ltr_override input ext-input text-box ext-text-box

# win-button button_primary button ext-button primary ext-primary

# form-control input ext-input text-box ext-text-box

# win-button button_primary button ext-button primary ext-primary
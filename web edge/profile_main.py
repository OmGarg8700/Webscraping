from selenium import webdriver
from selenium.webdriver.edge.options import Options
import pyautogui as gui
from time import sleep

array = ["Default", "Profile 1"]

edge_options = Options()
edge_options.use_chromium = True    
edge_options.add_argument("user-data-dir=C:\\Users\\91892\\AppData\\Local\\Microsoft\\Edge\\User Data")   

edge_options.add_argument("webdriver.edge.verboseLogging=true") 

def open_drivers(profile):
    edge_options.add_argument(f"profile-directory={profile}")
    try:
        webdriver.Edge(options = edge_options, executable_path="msedgedriver.exe")
    except:
        print("Error")
        

for i in array:
    open_drivers(i)


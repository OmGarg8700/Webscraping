from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

chrome_options = Options()

# chrome_options.add_argument(r'--user-data-dir=C:\Users\91892\AppData\Local\Google\Chrome\User Data\Default')
# chrome_options.add_argument('--profile-directory-Default')
chrome_options.add_experimental_option("debuggerAddress", "localhost:9988")

# driver = webdriver.Chrome("chromedriver", options=chrome_options)

def get_unread_messages(intitial, final):
    if(len(final) == 1 or len(initial) == 0):
        return 0
        
    last_message = initial[-1]

    count = 0
    for i in range(-1, -(len(final)-1), -1):
        if(last_message == final[i]):
            count = -i
            break
    return count

def make_report_messages(final, unread_messages, report_name = "report.txt", file_name = "output.txt"):
    #here making the latest time
    current_time = datetime.now()
    
    latest_time = str(current_time.day) + "/" + str(current_time.month) + "/" + str(current_time.year)

    final_report = []
    for i in range(-1, -unread_messages, -1):
        report = []
        list1 = final[i].split(" ")

        quantity = int(list1[0])
        description = " ".join(list1[1:len(list1)-1])
        rate = int(list1[-1])

        report.append(latest_time)
        report.append(quantity)
        report.append(description)
        report.append(rate)
        report.append(quantity*rate)

        final_report.append(report)
    
    with open(report_name, "a") as f:
        for i in range(len(final_report)):
            f.write(str(final_report[i]) + "\n")

    f.close()

    with open(file_name, "a") as f:
        for i in range(len(final_report)):
            for j in range(5):
                f.write(str(final_report[i][j]) + "\t\t")
            f.write("\n")
    f.close()

initial = []

count = 0

while(True):
    driver = webdriver.Chrome("chromedriver", options=chrome_options)
    driver.get("https://web.whatsapp.com")
    time.sleep(15)

    user_name = "Shivam Garg"

    user = driver.find_element("xpath" ,'//span[@title="{}"]'.format(user_name))
    user.click()
    
    # just appending the latest messages to final
    final = []
    for i in driver.find_elements("xpath", "//span[@class='i0jNr selectable-text copyable-text']//span"):
        final.append(i.text)

    # main work is going on
    if(initial != final):
        print(initial)
        print(final)
        unread_messages = get_unread_messages(initial, final)

        initial = final

        # unread messages coming from function is unread_messages + 1
        for i in range(-1, -unread_messages, -1):
            print(final[i])

        make_report_messages(final, unread_messages)

    driver.close()
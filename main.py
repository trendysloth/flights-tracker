import os  
import time
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By

CHROMEDRIVER_PATH='./chromedriver'
DATE='July 06'
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
DESTINATION = 'Shanghai'

class flights():
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver.get('https://www.united.com/')
    
    def submit_form(self):
        driver.find_element_by_id("oneway").click()
        destination = driver.find_element_by_id("bookFlightDestinationInput")
        destination.send_keys(DESTINATION)
        time.sleep(1)
        departDate = driver.find_element_by_id("DepartDate")
        departDate.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE )
        departDate.send_keys(DATE)
        time.sleep(2)
        driver.find_element_by_xpath("//html").click()
        driver.find_element_by_xpath("//html").click()
        time.sleep(5)
        driver.find_element_by_xpath('//span[text()="Find flights"]').click()
        time.sleep(5)
        
if __name__ == '__main__':
    flight = flights()
    flight.submit_form()
    # print(driver.find_element_by_css_selector("label[for='newfilter_stop']"))
    # driver.find_element_by_id('filter-stop-lowest-fare').click()
    # driver.find_element_by_xpath(xpath = "//section[@label='newfilter_stop']").click()
    # notification = driver.find_element_by_class_name('notification-block')
    # message = notification.getText()
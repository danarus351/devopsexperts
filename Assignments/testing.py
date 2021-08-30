from selenium import webdriver
from time import sleep
chrome_driver = '/home/ubuntu/Desktop/devops/Assignments/selenium_driver/chromedriver'
# firefox = webdriver.Firefox(executable_path='/home/ubuntu/Desktop/devops/Assignments/selenium_driver/geckodriver')
# assignment 5
try:
    chrome = webdriver.Chrome(executable_path=chrome_driver)
    chrome.get('https://github.com/')
    chrome.find_element_by_name('q').send_keys('Selenium')
    chrome.find_element_by_name('q').submit()
    sleep(5)

finally:
    chrome.close()
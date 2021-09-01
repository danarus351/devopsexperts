from selenium import webdriver
from time import sleep


try:
    firefox_driver = '/home/ubuntu/Desktop/devops/Assignments/selenium_driver/geckodriver'
    browser = webdriver.Firefox(executable_path=firefox_driver)
    browser.get('https://buyme.co.il/')
    sleep(3)
    browser.refresh()
    browser.find_element_by_xpath('/html/body/div[3]/div/header/div[1]/div/ul[1]/li[3]/a/span[2]').click()
    sleep(3)
    browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/div[3]/div[1]/span').click()
    browser.find_element_by_xpath('//*[@id="ember1482"]').send_keys('Dan')
    browser.find_element_by_xpath('//*[@id="ember1485"]').send_keys('danarus.d@gmail.com')
    browser.find_element_by_xpath('//*[@id="valPass"]').send_keys('Aa123456')
    browser.find_element_by_xpath('//*[@id="ember1491"]').send_keys('Aa123456')
    browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/div[3]/div[2]/div[3]/form/button/span").submit()

finally:
    browser.close()








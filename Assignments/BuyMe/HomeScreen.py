from selenium import webdriver
from time import sleep

try:
    firefox_driver = '/home/ubuntu/Desktop/devops/Assignments/selenium_driver/geckodriver'
    browser = webdriver.Firefox(executable_path=firefox_driver)
    browser.get('https://buyme.co.il/')
    sleep(3)
    browser.refresh()
    browser.find_element_by_xpath('/html/body/div[3]/div/header/div[3]/div/form/div[1]/a/span').click()
    html_list = browser.find_element_by_xpath('/html/body/div[3]/div/header/div[3]/div/form/div[1]/div/ul')
    options = html_list.find_elements_by_tag_name("li")
    for item in options:
        if item.text == 'מעל 750 ש"ח':
            item.click()
            break

    browser.find_element_by_xpath('/html/body/div[3]/div/header/div[3]/div/form/div[2]/a/span').click()
    html_list = browser.find_element_by_xpath('/html/body/div[3]/div/header/div[3]/div/form/div[2]/div/ul')
    options = html_list.find_elements_by_tag_name("li")
    for item in options:
        if item.text == 'ת"א והסביבה':
            item.click()
            break

    browser.find_element_by_xpath('/html/body/div[3]/div/header/div[3]/div/form/div[3]/a/span').click()
    html_list = browser.find_element_by_xpath('/html/body/div[3]/div/header/div[3]/div/form/div[3]/div/ul')
    options = html_list.find_elements_by_tag_name("li")
    for item in options:
        if item.text == 'מתנות עד הבית':
            item.click()
            break

    gift = browser.find_elements_by_partial_link_text('תמצאו לי מתנה')
    for item in gift:
        item.click()

    browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div/ul/li[14]/a/div/div[2]/span').click()

    sleep(5)
finally:
    browser.close()

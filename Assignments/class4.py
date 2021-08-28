# # assignment 1 +   2
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

firefox = webdriver.Firefox(executable_path='/home/ubuntu/Desktop/devops/Assignments/selenium_driver/geckodriver')
chrome = webdriver.Chrome(executable_path='/home/ubuntu/Desktop/devops/Assignments/selenium_driver/chromedriver')
try:
    chrome.get('https://www.walla.co.il/')
    sleep(1)
finally:
    chrome.close()

try:
    firefox.get('https://www.ynet.co.il')
    title = firefox.title
    firefox.refresh()
    print(title == firefox.name)
    sleep(5)

finally:
    firefox.close()
    chrome.close()

# assignment 3
#
# yes it is the same

# assignment 4
try:
    firefox.get('https://translate.google.com/')
    firefox.find_element_by_xpath('//*[@class="er8xn"]').send_keys('בננה')
    sleep(5)
finally:
    firefox.close()

# assignment 5
try:
    firefox.get('https://youtube.com/')
    firefox.find_element_by_xpath('//*[@name="search_query"]').send_keys('doja cat - women')
    firefox.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
    sleep(5)

finally:
    firefox.close()

# assignment 6

try:
    chrome.get('https://translate.google.com/')
    first_by_class = chrome.find_element_by_xpath('//*[@class="er8xn"]')
    second_by_arialabel = chrome.find_element_by_xpath('//*[@aria-label="Source text"]')
    third_by_ariacontrols = chrome.find_element_by_xpath('//*[@aria-controls="kvLWu"]')
    print(f'First WebElement: {first_by_class}\n'
          f'second WebElement: {second_by_arialabel}\n'
          f'third WebElement: {third_by_ariacontrols}')

finally:
    chrome.close()

# assignment 7

try:
    chrome.get('https://www.facebook.com/')
    chrome.find_element_by_name("email").send_keys('email')
    chrome.find_element_by_name('pass').send_keys('not remember')
    chrome.find_element_by_name("login").submit()
    sleep(10)


finally:
    chrome.close()

# assignment 8

try:
    chrome.get('https://www.facebook.com/')
    print(chrome.get_cookies())
    chrome.delete_all_cookies()
    print(chrome.get_cookies())

finally:
    chrome.close()

# assignment 9
try:
    chrome.get('https://github.com/')
    chrome.find_element_by_name('q').send_keys('Selenium')
    chrome.find_element_by_name('q').submit()
    sleep(5)

finally:
    chrome.close()

# # assignment 10
# try:
#
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-extensions")
#     chrome = webdriver.Chrome(executable_path='/home/ubuntu/Desktop/devops/Assignments/selenium_driver/chromedriver',
#                               chrome_options=chrome_options)
#     chrome.get('https://github.com/')
#     sleep(10)
#     firefox.get("https://github.com")
#     sleep(5)
#
# finally:
#     chrome.close()

# assignment 1

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path= 'D://DevOpsExperts//devopsexperts//class 4//chromedriver_win32//chromedriver.exe' )
browser.get('https://www.walla.co.il/')
sleep(1)
browser.close()

browser = webdriver.Firefox(executable_path='D://DevOpsExperts//devopsexperts//class 4//geckodriver-v0.29.1-win64//geckodriver.exe')
browser.get('https://www.ynet.co.il')
sleep(5)
browser.close()
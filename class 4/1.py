from selenium import webdriver
from time import sleep

browser = webdriver.Chrome(executable_path ='D://DevOpsExperts//devopsexperts//class 4//chromedriver_win32//chromedriver.exe')
browser.get("file://D://DevOpsExperts//devopsexperts//class 4//tip_calc_orig//index.html")
sleep(5)

browser.close()
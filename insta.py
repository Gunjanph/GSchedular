import os
import requests,sys,webbrowser,bs4
import urllib
import re
import time
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options
chrome_options = Options() 
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
mobile_emulation = { "deviceName": "Galaxy S5" }
# chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                        #  desired_capabilities = chrome_options.to_capabilities())

driver = webdriver.Chrome(executable_path=r"./chromedriver",options=chrome_options)
driver.get("https://www.instagram.com/")

username="autopostscheduler"
password="okmijnuhb"

element = driver.find_element_by_xpath("//button[text() = 'Log In']")
element.click() 

while(len(driver.find_elements_by_xpath("//input[@name='username']"))==0):
    time.sleep(1)
    print('Loading...')

username_button = driver.find_element_by_xpath("//input[@name='username']")
username_button.send_keys(username)
pass_button = driver.find_element_by_xpath("//input[@name='password']")
pass_button.send_keys(password)
while(len(driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']"))==0):
    time.sleep(1)
    print('Loading...')
element = driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
element[1].click() 

time.sleep(5)

while(len(driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']"))==0):
    time.sleep(1)
    print('sqdOP Loading...')

element = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
element.click() 

while(len(driver.find_elements_by_xpath("//button[@class='aOOlW   HoLwm ']"))==0):
    time.sleep(1)
    print('aOOlW Loading...')

element=driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
element.click() 


element=driver.find_element_by_xpath("//div[@class='q02Nz _0TPg']")
element.click()
element.send_keys(os.getcwd()+"/Test1.png") 

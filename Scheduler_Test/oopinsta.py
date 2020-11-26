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


username="autopostscheduler"
password="okmijnuhb"



class IGbot:
    def _init_(self,username,password):
        self.username=username
        self.password=password
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver",options=chrome_options)
        pass
    def login():
        # Open Insta
        self.driver.get("https://www.instagram.com/")

        #Login Page 1
        login_button_1 = self.driver.find_element_by_xpath("//button[text() = 'Log In']")
        login_button_1.click() 
        
        #Wait till the Login Input Page Opens
        while(len(self.driver.find_elements_by_xpath("//input[@name='username']"))==0):
            time.sleep(1)
            print('Loading...')

        #Find and send Username
        username_input = self.driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(self.username)
        
        #Find and send Password
        password_input = self.driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(self.password)
    
        #Final Login Click
        login_button_2 = self.driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
        login_button_2[1].click() 
        time.sleep(5)

        #Save your Login info - Not Now ( Doesnt matter)
        while(len(self.driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']"))==0):
            time.sleep(1)
            print('Save Information Loading...')

        element = self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
        element.click() 

        # Turn on Notification - Not Now
        while(len(self.driver.find_elements_by_xpath("//button[@class='aOOlW   HoLwm ']"))==0):
            time.sleep(1)
            print('Notification Loading...')

        element=self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
        element.click() 
        print("Login Compleat")
    
    def upload():
        upload_button=self.driver.find_element_by_xpath("//div[@class='q02Nz _0TPg']")
        upload_button.click()
        # element.send_keys(os.getcwd()+"/Test1.png") 

        os.system('autokey-run -s select_image')

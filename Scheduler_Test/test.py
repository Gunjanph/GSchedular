from selenium import webdriver

username = "Your Username"
password = "Your Password"

getdriver = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Firefox()
driver.get(getdriver)

driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
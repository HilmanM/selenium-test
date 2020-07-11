from selenium import webdriver
import time

# Opening The Browser
driver = webdriver.Firefox()
driver.get("https://twitter.com/")

# Xpath Element of the website
email_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[1]/div/label/div/div[2]/div/input'
password_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[2]/div/label/div/div[2]/div/input'
login_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/section/form/div/div[3]/div'
status_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
photo_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/input'
tweet_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]'

# Selecting The Element of The login Form
email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

# Send Input to The Form
email_element.send_keys('samigo2171@djemail.net')
password_element.send_keys('testtest123')

# Click The Login
time.sleep(1)
login_button_element.click()

# Uploading The picture
time.sleep(1)
photo_element = driver.find_element_by_xpath(photo_xpath)
photo_element.send_keys('/home/maulana/selenium-test/test-pic.jpg')

# Input Text Status
time.sleep(2)
status_element = driver.find_element_by_xpath(status_xpath)
status_element.send_keys('this status new')

# Click Tweet button
time.sleep(1)
tweet_button_element = driver.find_element_by_xpath(tweet_button_xpath)
tweet_button_element.click()
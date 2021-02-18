import sys

gecko_folder_path = "C:\selenium\selenium-java\ChromeDriver\chromedriver.exe"
sys.path.append(gecko_folder_path)
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get("https://www.thesparksfoundationsingapore.org/")

print("\nLet's Check For The TestCases:\n")

# TestCase 1: Title
print("TestCase #1:")
if (driver.title):
    print("Title Verification Successful: ", driver.title)
else:
    print("Title Verification Failed!\n")

# TestCase 2: Home button
print("TestCase #2:")
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Home link works!\n")
except NoSuchElementException:
    print("Home Link Doesn't Work!\n")

# TestCase 3: Check if navbar appears
print("TestCase #3:")
try:
    driver.find_element_by_class_name("navbar")
    print("Navbar Verification Successful!\n")
except NoSuchElementException:
    print("Navbar Verification Failed!\n")

# TestCase 4: About Us Page
print("TestCase #4:")
try:
    driver.find_element_by_link_text('About Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Vision, Mission and Values').click()
    time.sleep(3)
    print('Page visited Successfully!\n')
except NoSuchElementException:
    print("Page visit Failed! Does not exist.\n")
    time.sleep(3)

# TestCase 5: Policies and Code
print('TestCase #5:')
try:
    driver.find_element_by_link_text('Policies and Code').click()
    time.sleep(3)
    driver.find_element_by_link_text("Policies").click()
    time.sleep(3)
    print('Policy page exists. Success!\n')
except NoSuchElementException:
    print('Policy Page Does not exist. Failed!\n')
    time.sleep(3)

# TestCase 6: Workshop page
print('TestCase #6:')
try:
    driver.find_element_by_link_text('Programs').click()
    time.sleep(3)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(3)
    driver.find_element_by_link_text('LEARN MORE').click()
    time.sleep(3)
    print('Workshop Page Verified!\n')
except NoSuchElementException:
    print('No New Tab opened. Failed!\n')

# TestCase 7: Links Page
print("TestCase #7")
try:
    driver.find_element_by_link_text('LINKS').click()
    time.sleep(3)
    driver.find_element_by_link_text('Software & App').click()
    time.sleep(3)
    driver.find_element_by_link_text('Visit LINKS @TSF').click()
    time.sleep(3)
    print('LINKS Verfication successful!\n')
except NoSuchElementException:
    print("LINKS Verification Failed!\n")

# TestCase 8: Check If Logo Exists
print('TestCase #8:')
try:
    driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/*').click()
    print('Found Logo! Success!\n')
    time.sleep(3)
except NoSuchElementException:
    print('No logo found!\n')

# TestCase 9:   Check the Form
print("TestCase #9:")
try:
    driver.find_element_by_link_text('Join Us').click()
    time.sleep(3)
    driver.find_element_by_link_text('Why Join Us').click()
    time.sleep(3)
    driver.find_element_by_name('Name').send_keys('Aiman')
    time.sleep(3)
    driver.find_element_by_name('Email').send_keys('aiman@gmail.com')
    time.sleep(3)
    select = Select(driver.find_element_by_class_name('form-control'))
    time.sleep(3)
    select.select_by_visible_text('Student')
    time.sleep(3)
    driver.find_element_by_class_name('button-w3layouts').click()
    time.sleep(3)
    print("Form Verification Successful!\n")
    time.sleep(3)
except NoSuchElementException:
    print("Form Verification Failed!\n")
    time.sleep(3)

# TestCase 10:   Check the Contact us Page
print("TestCase #10:")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(3)
    info = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[3]/div[2]/p[2]')
    time.sleep(3)

    # print(info.text)
    if (info.text == "+65-8402-8590, info@thesparksfoundation.sg"):
        print('contact Information Correct!')
    else:
        print('Contact Information Incorrect!')

    # assert driver.page_source.find("+65-8402-859, info@thesparksfoundation.sg")
    print("Contact Page Verification Sucessful!\n")
except NoSuchElementException:
    print("Contact Page Verification unsuccessful!")
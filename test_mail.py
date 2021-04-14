from selenium import webdriver
from test_locators import LOCATORS
import pytest
import time
    
def test_mail():
    driver = webdriver.Chrome()
    driver.get(LOCATORS.url)
    driver.maximize_window()
    driver.find_element_by_css_selector(LOCATORS.login_input).send_keys(LOCATORS.mail_address)
    driver.find_element_by_css_selector(LOCATORS.password_input).send_keys(LOCATORS.password)
    driver.find_element_by_css_selector(LOCATORS.submit_button).click()
    time.sleep(2)
    driver.find_element_by_xpath(LOCATORS.letter_button).click()
    driver.find_element_by_css_selector(LOCATORS.mail_field).send_keys(LOCATORS.mail_address+LOCATORS.domain_name)
    driver.find_element_by_css_selector(LOCATORS.subject).send_keys(LOCATORS.subject_text)
    driver.find_element_by_xpath(LOCATORS.text_field).send_keys(LOCATORS.test_text)
    driver.find_element_by_css_selector(LOCATORS.send_button).click()
    time.sleep(2)
    driver.find_element_by_css_selector(LOCATORS.back_button).click()
    time.sleep(2)
    driver.find_element_by_xpath(LOCATORS.open_mail_button).click()
    time.sleep(2)
    my_mail = driver.find_element_by_css_selector(LOCATORS.search_text)
    assert LOCATORS.test_text in my_mail.text
    driver.quit()


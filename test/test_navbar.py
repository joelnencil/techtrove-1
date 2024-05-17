# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNavbar():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_navbar(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1050, 660)
    self.driver.find_element(By.LINK_TEXT, "Products").click()
    self.driver.find_element(By.LINK_TEXT, "Account").click()
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(3) > img").click()
  
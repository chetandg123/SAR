import os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

from Data.parameters import Data


class cqube():

    def __init__(self, driver):
        self.driver = driver

    def open_cqube_appln(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(Data.url)

    def login_cqube(self):
        self.driver.find_element_by_xpath(Data.email).send_keys(Data.username)
        self.driver.find_element_by_xpath(Data.pwd).send_keys(Data.password)
        self.driver.find_element_by_xpath(Data.loginbtn).click()

    def navigate_to_student_report(self):
        self.driver.find_element_by_xpath(Data.Dashboard).click()
        self.driver.find_element_by_xpath(Data.SAR).click()

    def select_month_year(self,y,m):
        year = Select(self.driver.find_element_by_name(Data.select_year))
        month = Select(self.driver.find_element_by_name(Data.select_month))
        time.sleep(2)
        year.select_by_visible_text(y)
        time.sleep(2)
        month.select_by_visible_text(m)
        time.sleep(2)


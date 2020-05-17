from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


class BasePage(object):

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.timeout = 30

    def _open(self):
        self.driver.get(self.url)

    def open(self):
        self._open()

    def find_element(self,*locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException as e:
            raise e

class PageElement(BasePage):

    #模拟点击找到的元素节点
    def click_element(self,*loc):
        self.find_element(*loc).click()







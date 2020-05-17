import unittest
import sys
sys.path.append('E:\\AutoTest\\auto-test-demo')
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from page.searchPage import SearchPage
from common.common_information import Url,Locator
from time import sleep

class TestBaiduPage(unittest.TestCase):

    '''
    初始化
    '''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = Url.url
        self.pa = SearchPage(self.driver,self.url)
        self.pa.open()
        self.driver.maximize_window()

    '''
    关闭连接
    '''
    def tearDown(self):
        self.driver.close()

    '''
    测试新闻页
    '''
    def test_news(self):
        target_news = SearchPage.news_content
        self.pa.click_element(*Locator.news)
        sleep(2)
        #断言
        self.assertIn(target_news,self.driver.page_source)

    '''
    测试hao123主页
    '''
    def test_hao(self):
        target_hao = SearchPage.hao_content
        self.pa.click_element(*Locator.hao)
        sleep(2)
        #断言
        self.assertIn(target_hao,self.driver.page_source)

    '''
    测试百度贴吧
    '''
    def test_tieba(self):
        target_tieba = SearchPage.tieba_content
        self.pa.click_element(*Locator.tieba)
        sleep(2)
        # 断言
        self.assertIn(target_tieba, self.driver.page_source)

if __name__ == '__main__':
    unittest.main()





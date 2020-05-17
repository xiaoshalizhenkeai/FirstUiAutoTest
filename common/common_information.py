from selenium.webdriver.common.by import By

"""
存放网站的地址
"""
class Url():
    url = 'https://www.baidu.com'

"""
存放待测试的元素定位
"""
class Locator():

    news = (By.LINK_TEXT,'新闻')
    hao = (By.NAME,'tj_trhao123')
    tieba = (By.NAME,'tj_trtieba')
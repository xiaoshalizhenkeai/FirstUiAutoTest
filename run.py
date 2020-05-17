from unittest import *
import HTMLTestRunner
import time
from common.sendEmail import *
import unittest

def get_test_cases(dirpath):
    '''
    :param dirpath: 测试用例文件存放的路径
    :return: 返回用例测试套件
    '''
    #测试套件，存放测试用例
    test_cases = unittest.TestSuite()
    #测试用例以"test开头"，将所有的测试用例加载出来
    suites = unittest.defaultTestLoader.discover(dirpath,'test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

if __name__ == '__main__':
    cases = get_test_cases('./testcase')
    #测试报告生成时间
    now = time.strftime("%Y-%m-%d %H:%M")
    test_report_path = ('./report')
    file_name ='./report' + now + 'report.html'
    fp = open(file_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=1, title=u"百度首页子项测试报告", description=u'详细测试情况如下:')
    runner.run(cases)
    fp.close()
    time.sleep(8)
    new_report_path = acquire_report_address(test_report_path)
    #发送邮件
    send_email(new_report_path)







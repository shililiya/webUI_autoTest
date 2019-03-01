import unittest
import HTMLTestRunner
import os
from testsuites.test_send_reply import DiscuzSendReply
from testsuites.test_delete import DiscuzDelete
from testsuites.test_search import DiscuzSearch
from testsuites.test_vote import Vote
import time
#设置报告文件的保存路径

report_path=os.path.dirname(os.path.abspath('.'))+'/reporter/'
now=time.strftime(('%Y-%m-%d-%H_%M_%S'),time.localtime(time.time()))
if not os.path.exists(report_path):os.mkdir(report_path)
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSendReply))
suite.addTest(unittest.makeSuite(DiscuzDelete))
suite.addTest(unittest.makeSuite(DiscuzSearch))
suite.addTest(unittest.makeSuite(Vote))

if __name__=="__main__":
    html_report=report_path+r"\_result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="论坛测试报告",description="论坛用例执行情况")
    runner.run(suite)
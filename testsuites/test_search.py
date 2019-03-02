import unittest
from testsuites.base_testcase import BaseTestCase
from pageobject.discuz_homepage import HomePage
from pageobject.discuz_search import Search
class DiscuzSearch(BaseTestCase):
    def test_search(self):
        home_page=HomePage(self.driver)
        home_page.login('lixiaoting','123456')
        loginAssert=home_page.loginAssertPanduan()
        self.assertEqual(loginAssert,'lixiaoting',msg=loginAssert)
        discuz_search = Search(self.driver)
        discuz_search.search('haotest')
        #测试断言
        result=discuz_search.assertPanduan()
        # 测试退出
        discuz_search.tuichu()
        self.assertEqual(result, "haotest", msg=result)
if __name__=='__main':
    unittest.main()
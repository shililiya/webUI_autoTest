import unittest
from testsuites.base_testcase import BaseTestCase
from pageobject.discuz_homepage import HomePage
from pageobject.discuz_delete import Delete
import time
class DiscuzDelete(BaseTestCase):
    def test_delete(self):
        home_page = HomePage(self.driver)
        deleteTie = Delete(self.driver)
        # 测试管理员登录
        home_page.login('admin', 'hemeihua')
        loginAssert=home_page.loginAssertPanduan()
        self.assertEqual(loginAssert,'admin',msg=loginAssert)
        time.sleep(5)
        home_page.moren()

        deleteTie.delete()
        deleteTie.discuz('hemeihua')
        deleteTie.buildDiscuz()
        deleteTie.discuzExit()
        # 管理员退出
        deleteTie.adminExit()
        #普通用户登录
        home_page.login('lixiaoting','123456')
        commonLogin=home_page.loginAssertPanduan()
        self.assertEqual(commonLogin,'lixiaoting',msg=commonLogin)
        deleteTie.send('幸运','啦啦啦啦啦啦啦啦啦啦啦啦啦啦')
        deleteTie.reply('每天都要加油啊啦啦啦啦啦啦啦啦啦啦啦啦啦')

if __name__=="__main__":
    unittest.main()
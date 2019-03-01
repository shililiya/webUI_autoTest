import unittest
from testsuites.base_testcase import BaseTestCase
from pageobject.discuz_homepage import HomePage
from pageobject.discuz_delete import Delete
import time
class DiscuzDelete(BaseTestCase):
    def test_delete(self):
        home_page = HomePage(self.driver)
        # 测试管理员登录
        home_page.login('admin', 'Lxt69290*.')
        time.sleep(5)
        home_page.moren()
        deleteTie = Delete(self.driver)
        deleteTie.delete()
        deleteTie.discuz('Lxt69290*.')
        deleteTie.discuzExit()
        # 管理员退出
        deleteTie.adminExit()
        #普通用户登录
        home_page.login('lixiaoting','123456')
        deleteTie.send('幸运','啦啦啦啦啦啦啦啦啦啦啦啦啦啦')
        deleteTie.reply('每天都要加油啊啦啦啦啦啦啦啦啦啦啦啦啦啦')

if __name__=="__main__":
    unittest.main()
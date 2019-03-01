import unittest
from testsuites.base_testcase import BaseTestCase
from pageobject.discuz_homepage import HomePage
from pageobject.discuz_send_reply import SendReply
class DiscuzSendReply(BaseTestCase):
    def test_send_reply(self):
        #测试普通用户登录
        home_page=HomePage(self.driver)
        home_page.login('lixiaoting','123456')
        home_page.moren()
        #测试发帖
        send_reply=SendReply(self.driver)
        send_reply.send("这是题目","这是我写的内容，啦啦")
        send_reply.reply("这是我给你的回复")
        #测试普通用户退出
        home_page.exit()
if __name__=="__main__":
    unittest.main()

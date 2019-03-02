import unittest
from testsuites.base_testcase import BaseTestCase
from pageobject.discuz_homepage import HomePage
from pageobject.discuz_vote import DiscuzVote
import time
class Vote(BaseTestCase):
    def test_vote(self):
        home_page=HomePage(self.driver)
        home_page.login('lixiaoting','123456')
        time.sleep(5)
        loginAssert=home_page.loginAssertPanduan()
        self.assertEqual(loginAssert,'lixiaoting',msg=loginAssert)
        home_page.moren()
        discuz_vote=DiscuzVote(self.driver)
        discuz_vote.discuzVote("啦啦啦","我是卖报的小行家","不等天明来卖报")
        subjectAssert=discuz_vote.voteSubjectAssert()
        self.assertEqual(subjectAssert,'啦啦啦',msg=subjectAssert)
        time.sleep(2)
        discuz_vote.submit()
        time.sleep(2)
        discuz_vote.name_percent()
        home_page.exit()
if __name__=="__main__":
    unittest.main()
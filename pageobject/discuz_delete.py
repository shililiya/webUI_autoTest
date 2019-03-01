from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class Delete(BasePage):
    home_page_small_box_loc=(By.CSS_SELECTOR,'.o input')
    home_page_delete_loc=(By.LINK_TEXT,'删除')
    home_page_submit_loc=(By.CSS_SELECTOR,'.o button')
    home_page_manage_loc=(By.LINK_TEXT,'管理中心')
    home_page_pwd_input_loc=(By.CSS_SELECTOR,'.loginform input')
    home_page_submit_button_loc=(By.CSS_SELECTOR,'.loginnofloat input')
    home_page_discuz_loc=(By.XPATH,'//ul/li[7]')
    home_page_discuz_build_bankuai_loc=(By.CSS_SELECTOR,'.lastboard .addtr')
    home_page_discuz_submit_new_loc=(By.CSS_SELECTOR,'.fixsel input')
    home_page_discuz_exit_loc=(By.CSS_SELECTOR,'.mainhd .uinfo a')
    home_page_new_send_loc=(By.CSS_SELECTOR,'.bm_c table tr:nth-last-child(2) td:nth-last-child(3) h2 a')
    home_page_new_send_title_loc=(By.CSS_SELECTOR,'.pbt input')
    home_page_new_send_content_loc=(By.CSS_SELECTOR,'.area .pt')
    home_page_submit_fatie_loc=(By.CSS_SELECTOR,'.ptm button')
    home_page_reply_content_loc=(By.CSS_SELECTOR,'.area .pt')
    home_page_submit_reply_loc=(By.CSS_SELECTOR,'.ptm .pn')
    home_page_admin_exit_loc=(By.LINK_TEXT,'退出')
    def delete(self):
        self.jihuo(0)
        self.click(*self.home_page_small_box_loc)
        self.click(*self.home_page_delete_loc)
        self.click(*self.home_page_submit_loc)
        self.click(*self.home_page_manage_loc)
    def discuz(self,pwd):
        time.sleep(5)
        self.jihuo(1)
        self.sendkeys(pwd,*self.home_page_pwd_input_loc)
        self.click(*self.home_page_submit_button_loc)
        time.sleep(2)
        self.click(*self.home_page_discuz_loc)
        time.sleep(3)
        self.driver.switch_to.frame(0)
        self.click(*self.home_page_discuz_build_bankuai_loc)
        self.click(*self.home_page_discuz_submit_new_loc)
    def discuzExit(self):
        self.jihuo(1)
        self.click(*self.home_page_discuz_exit_loc)
        time.sleep(5)
    def adminExit(self):
        self.jihuo(1)
        self.click(*self.home_page_admin_exit_loc)
        self.jihuo(1)
    def send(self,title,content):
        time.sleep(5)
        self.click(*self.home_page_new_send_loc)
        time.sleep(5)
        self.sendkeys(title,*self.home_page_new_send_title_loc)
        self.sendkeys(content,*self.home_page_new_send_content_loc)
        self.click(*self.home_page_submit_fatie_loc)
        time.sleep(2)
    def reply(self,content):
        self.jihuo(1)
        self.sendkeys(content,*self.home_page_reply_content_loc)
        self.click(*self.home_page_submit_reply_loc)


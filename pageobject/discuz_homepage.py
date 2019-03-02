from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class HomePage(BasePage):
    home_page_input_name_loc=(By.NAME,"username")
    home_page_input_pwd_loc=(By.NAME,"password")
    home_page_login_loc=(By.CSS_SELECTOR,'.fastlg_l>button')
    home_page_login_assert_loc = (By.CSS_SELECTOR, '.vwmy a')
    home_page_moren_loc = (By.CSS_SELECTOR, '.bm_c h2 a')
    home_page_exit_loc=(By.LINK_TEXT,'退出')
    def login(self,name,pwd):
        self.sendkeys(name,*self.home_page_input_name_loc)
        self.sendkeys(pwd,*self.home_page_input_pwd_loc)
        self.click(*self.home_page_login_loc)
        time.sleep(5)

    def moren(self):
        self.click(*self.home_page_moren_loc)

    def exit(self):
        self.click(*self.home_page_exit_loc)

    def loginAssertPanduan(self):
        time.sleep(5)
        result=self.getText(*self.home_page_login_assert_loc)
        return result


from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class Search(BasePage):
    home_page_search_loc=(By.CSS_SELECTOR,'.scbar_txt_td input')
    home_page_search_button=(By.CSS_SELECTOR,'.scbar_btn_td button')
    home_page_title_loc = (By.CSS_SELECTOR, '.xs3 a strong font')
    home_page_tuichu_loc=(By.CSS_SELECTOR,'.y a:nth-child(4)')
    def search(self,content):
        self.sendkeys(content,*self.home_page_search_loc)
        self.click(*self.home_page_search_button)
        self.jihuo(1)
    def assertPanduan(self):
        time.sleep(5)
        result=self.getText(*self.home_page_title_loc)
        return result
    def tuichu(self):
        self.jihuo(1)
        self.click(*self.home_page_tuichu_loc)

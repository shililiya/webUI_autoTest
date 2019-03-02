from framework.base import BasePage
from selenium.webdriver.common.by import By
import time
class SendReply(BasePage):
    home_page_send_title_loc = (By.CSS_SELECTOR,'.pbt>input')
    home_page_send_content_loc = (By.CSS_SELECTOR,'.area .pt')
    home_page_fatie_button_loc = (By.CSS_SELECTOR, ".ptm button ")
    home_page_reply_context_loc = (By.CSS_SELECTOR, ".tedt .area .pt")
    home_page_moren_assert_loc=(By.CSS_SELECTOR,'.xs2 a')
    home_page_reply_button_loc = (By.CSS_SELECTOR, ".ptm .pn")
    def send(self, title, content):
        self.sendkeys(title, *self.home_page_send_title_loc)
        self.sendkeys(content, *self.home_page_send_content_loc)
        self.click(*self.home_page_fatie_button_loc)

    def reply(self, content):
        self.sendkeys(content, *self.home_page_reply_context_loc)
        self.click(*self.home_page_reply_button_loc)

    def morenAssertPanduan(self):
        result=self.getText(*self.home_page_moren_assert_loc)
        return result


from framework.base import BasePage
from selenium.webdriver.common.by import By
from framework.logger import Logger
logger=Logger(logger="DiscuzVote").getlog()
import time
class DiscuzVote(BasePage):
    home_page_fatie_button_loc = (By.CSS_SELECTOR, '.bw0> a')
    home_page_vote_button_loc = (By.CSS_SELECTOR,'.mbw li:nth-child(2) a')
    home_page_vote_title_input_loc=(By.CSS_SELECTOR,'.pbt .z span input')
    home_page_first_input_loc=(By.CSS_SELECTOR,'.mbm p input')
    home_page_second_input_loc=(By.CSS_SELECTOR,'.mbm p:nth-child(2) input')
    home_page_sendVote_button_loc=(By.CSS_SELECTOR,'.pnpost .pn span')
    home_page_vote_radio_button_loc=(By.CSS_SELECTOR,'.pcht .pslt')
    home_page_submit_vote_loc=(By.CSS_SELECTOR,'.pcht table tr:nth-last-child(1) button')
    home_page_first_text_loc=(By.CSS_SELECTOR,'.pvt label')
    home_page_first_percent_loc=(By.CSS_SELECTOR,'.pcht tr:nth-child(2) td:nth-child(2)')
    home_page_second_text_loc=(By.CSS_SELECTOR,'.pcht tr:nth-child(3) label')
    home_page_second_percent_loc=(By.CSS_SELECTOR,'.pcht tr:nth-child(4) td:nth-child(2)')
    home_page_vote_subject_name_loc=(By.CSS_SELECTOR,'.ts span')
    def discuzVote(self,subject,first,second):
        self.click(*self.home_page_fatie_button_loc)
        self.jihuo(0)
        self.click(*self.home_page_vote_button_loc)
        time.sleep(2)
        self.sendkeys(subject,*self.home_page_vote_title_input_loc)
        self.sendkeys(first,*self.home_page_first_input_loc)
        self.sendkeys(second,*self.home_page_second_input_loc)
        self.click(*self.home_page_sendVote_button_loc)
        self.jihuo(0)
    def submit(self):
        time.sleep(2)
        self.click(*self.home_page_vote_radio_button_loc)
        time.sleep(2)
        self.click(*self.home_page_submit_vote_loc)
        time.sleep(2)
    def name_percent(self):
        first_name=self.getText(*self.home_page_first_text_loc)
        logger.info("第一个选项的名称：%s"%first_name)
        first_percent=self.getText(*self.home_page_first_percent_loc)
        logger.info("第一个选项的投票比例：%s"%first_percent)
        second_name=self.getText(*self.home_page_second_text_loc)
        logger.info("第二个选项的名字：%s"%second_name)
        second_percent=self.getText(*self.home_page_second_percent_loc)
        logger.info("第二个选项的投票比例：%s"%second_percent)
        subject_name=self.getText(*self.home_page_vote_subject_name_loc)
        logger.info("投票的主题名称为：%s"%subject_name)
    def voteSubjectAssert(self):
        result=self.getText(*self.home_page_vote_subject_name_loc)
        return result
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import os
import time

logger=Logger(logger="BasePage").getlog()    #希望输出哪个类输出的信息

class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
    def back(self):
        self.driver.back()
        logger.info("浏览器后退")
    def forward(self):
        self.driver.forward()
        logger.info("浏览器前进")
    def open_url(self,url):
        self.driver.get(url)
    def quit_broswer(self):
        self.driver.quit()
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭当前页面")
            self.get_window_img()
        except Exception as e:
            logger.error("关闭失败"%e)
            self.get_window_img()
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            ele=self.driver.find_element(*loc)
            # logger.info("找到页面元素%s" *loc)
            self.get_window_img()
            return ele

        except:
            logger.error("%s页面中未找到%s元素"%(self,loc))
            self.get_window_img()
    def sendkeys(self,text,*loc):
        el = self.find_element(*loc)
        try:
            el.send_keys(text)
            logger.info("输入内容：%s" % text)
            self.get_window_img()
        except Exception as e:
            logger.error("输入内容失败：%s" %e)
            self.get_window_img()
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("清除成功")
            self.get_window_img()
        except Exception as e:
            logger.error("清除失败:%s"%e)
            self.get_window_img()
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("click")
            self.get_window_img()
        except Exception as e:
            logger.error("单击失败%s"%e)
            self.get_window_img()
    def jihuo(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])
    def getText(self,*loc):
        el=self.find_element(*loc)
        try:
            content=el.text
            logger.info("帖子和期望值一样:%s" %content)
            self.get_window_img()
            return content

        except Exception as e:
            logger.info("帖子和期望值不同:%s"%e)
            self.get_window_img()
    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/img"
        if not os.path.exists(file_path): os.mkdir(file_path)
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("有截屏且保存路径是/img/")
        except Exception as e:
            logger.error("%s截屏失败"%e)


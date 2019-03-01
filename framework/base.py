from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger

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
        except Exception as e:
            logger.error("关闭失败"%e)
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            ele=self.driver.find_element(*loc)
            # logger.info("找到页面元素%s" *loc)
            return ele
        except:
            logger.error("%s页面中未找到%s元素"%(self,loc))
    def sendkeys(self,text,*loc):
        el = self.find_element(*loc)
        try:
            el.send_keys(text)
            logger.info("输入内容：%s" % text)
        except Exception as e:
            logger.error("输入内容失败：%s" %e)
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("清除成功")
        except Exception as e:
            logger.error("清除失败:%s"%e)
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("click")
        except Exception as e:
            logger.error("单击失败%s"%e)
    def jihuo(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])
    def getText(self,*loc):
        el=self.find_element(*loc)
        try:
            content=el.text
            return content
            logger.info("帖子和期望值一样:%s"%content)
        except Exception as e:
            logger.info("帖子和期望值不同:%s"%e)



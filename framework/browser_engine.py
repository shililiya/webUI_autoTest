import os.path
from configparser import ConfigParser  #读取config文件   专门做config文件的处理
from selenium import webdriver
from framework.logger import Logger
logger=Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+'/tools/chromedriver.exe'
    ie_driver_path=dir+'/tools/IEDriverServer.exe'
    firefox_driver_path=dir+'/tools/geckodriver.exe'

    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser=config.get("browserType","browserName")
        logger.info("你选择%s浏览器"%browser)
        url=config.get("testServer","URL")
        logger.info("这个服务器的地址是：%s"%url)

        if browser=="Firefox":
            self.driver=webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("开始火狐浏览器")
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("开始谷歌浏览器")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("开始IE浏览器")
        self.driver.get(url)
        logger.info("打开地址：%s"%url)
        self.driver.maximize_window()
        logger.info("最大化当前窗口")
        self.driver.implicitly_wait(10)
        logger.info("设置隐式等待时间为10秒")
        return self.driver
    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()
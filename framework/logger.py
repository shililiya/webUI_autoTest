import logging
import os
import time
class Logger(object):   #objeck是所有类的基类，可写可不写
    def __init__(self,logger):
        #创建一个logger对象
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)    #设置一个日志级别

        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+"/logs/"
        log_name=log_path+rq+".log"
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        fh=logging.FileHandler(log_name)

        fh.setLevel(logging.INFO)
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        #设置输出规则
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
    def getlog(self):
        return self.logger
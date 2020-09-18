# -*- encoding: utf-8 -*-
import os
import time
import logging
import logging.handlers

# logging初始化工作
logging.basicConfig()

# myapp的初始化工作
myapp = logging.getLogger('myapp')
myapp.setLevel(logging.INFO)

file_name = os.path.join('./', 'log1', 'myapp')
# 添加TimedRotatingFileHandler
# 定义一个1秒换一次log文件的handler
# 保留3个旧log文件
timefilehandler = logging.handlers.TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=5)
# 设置后缀名称，跟strftime的格式一样
# timefilehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
timefilehandler.suffix = "%Y-%m-%d.log"

formatter = logging.Formatter('%(asctime)s|%(name)-12s: %(levelname)-8s %(message)s')
timefilehandler.setFormatter(formatter)
myapp.addHandler(timefilehandler)

while True:
    time.sleep(0.1)
    myapp.info("test")

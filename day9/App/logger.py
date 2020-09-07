# -*- encoding: utf-8 -*-
"""
@File    : logger.py
@Time    : 2020/8/14 11:12
@Author  : zhangjun
@Email   : 123aaaasule@163.com
@Software: PyCharm
"""
# -*- coding:utf-8 -*-

import logging
import os
from logging import handlers
from os import path
import time

project_path = path.abspath(path.dirname(path.dirname(__file__)))

# 第一步 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步 创建一个handler 用于写入日志文件
rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))[:-6]
log_path = project_path + "/logs/"
log_name = log_path + rq + '.log'
logfile = log_name

fh = logging.FileHandler(logfile, mode='a', encoding="utf-8")

fh.setLevel(logging.INFO)  # 输出到file的log等级的开关

# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)

# 第四步，将logger添加到handler里面
logger.addHandler(fh)

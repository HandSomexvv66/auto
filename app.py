import os
import logging
import logging.handlers
# 封装url
import time

url = 'http://182.92.81.159/api/sys/'

# 封装path

path1 = os.path.dirname(os.path.abspath(__file__))
print(path1)

def log():

    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建控制台处理器
    sh = logging.StreamHandler()
    #文件处理器
    filename = path1+'/log/{}.html'.format(time.strftime('%H%M%S'))
    fie = logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=2, encoding='utf-8')


    # 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)]  %(message)s'
    format = logging.Formatter(fmt)

    # 将格式化器添加到处理器
    sh.setFormatter(format)
    fie.setFormatter(format)

    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fie)
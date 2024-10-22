# logger

import os
import logging
from logging.handlers import TimedRotatingFileHandler

from config import BASE_PATH



class GetLog:
    # 定义类属性保存日志器
    __logger = None

    # 获取日志器
    @classmethod
    def get_logger(cls):
        # 如果 __logger为空， 无法获取，需要先创建保存到__logger
        if cls.__logger is None:
            # 创建日志器
            cls.__logger = logging.getLogger("logger")
            cls.__logger.setLevel(logging.INFO)

            # 构建日志文件路径
            log_path = BASE_PATH + os.sep + "log" + os.sep + "hmtt.log"

            # 创建处理器
            tr = TimedRotatingFileHandler(filename=log_path,
                                            when="midnight",        #
                                            interval=1,             # 间隔
                                            backupCount=5,          # 备份的数量
                                            encoding='utf-8')
            # 创建格式化器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt=fmt)
            # 处理器设置格式
            tr.setFormatter(fm)
            # 日志器添加处理器
            cls.__logger.addHandler(tr)

        # 返回日志器
        return cls.__logger

if __name__ == '__main__':
    log = GetLog.get_logger()
    log.info("测试信息级别日志")
    log.error("测试错误级别日志")
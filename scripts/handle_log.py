import logging
import os
from scripts.handle_config import config_read_file
from scripts.constant import LOG_DIR

class HandleLog:
    """
    封装日志
    """
    def __init__(self):
        
        # 1、定义日志收集器
        self.logger = logging.getLogger(config_read_file.get_value("log", "log_name"))
        self.logger.setLevel(config_read_file.get_value("log", "log_level"))
        
        # 2、定义输出渠道
        # 定义日志输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(config_read_file.get_value("log", "console_level"))
        # 定义日志输出到文件
        fh = logging.FileHandler(os.path.join(LOG_DIR, config_read_file.get_value("log", "log_filename")),encoding="utf8")
        fh.setLevel(config_read_file.get_value("log", "file_level"))
        
        # 3、定义输出的 格式
        simple_formatter = logging.Formatter(config_read_file.get_value("log", "simple_formatter"))
        complex_formatter = logging.Formatter(config_read_file.get_value("log", "complex_formatter"))

        # 4、对接日志输出格式
        ch.setFormatter(simple_formatter)
        fh.setFormatter(complex_formatter)
        
        # 5、对接
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger

do_logger = HandleLog()
logger = do_logger.get_logger()
# ceshi
if __name__=="__main__":
    do_logger = HandleLog()
    logger = do_logger.get_logger()
    logger.debug("输出debug信息")
    logger.info("输出info信息")
    logger.error("输出error信息")
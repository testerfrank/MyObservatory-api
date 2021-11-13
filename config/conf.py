#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

from utils.utils_time import dt_strftime


class ConfigManager:
    """目录管理"""
    # 项目根目录
    BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 测试数据目录
    TESTDATA_DIR = os.path.join(BASEDIR, "data", "test_data")
    # 测试报告
    REPORT_DIR = os.path.join(BASEDIR, "report")
    # API请求数据目录
    API_DIR = os.path.join(BASEDIR, "data", "request_data")

    @property
    def log_file(self):
        """日志文件"""
        log_dir = os.path.join(self.BASEDIR, "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file = os.path.join(log_dir, "{}.log".format(dt_strftime()))
        return file

    @property
    def ini_file(self):
        """config.ini配置文件"""
        ini_file = os.path.join(self.BASEDIR, "config", "config.ini")
        if not os.path.exists(ini_file):
            raise FileNotFoundError(f"{ini_file}配置文件不存在！")
        return ini_file


cm = ConfigManager()
if __name__ == "__main__":
    print("项目根目录：{}".format(cm.BASEDIR))
    print("测试数据目录：{}".format(cm.DATA_DIR))
    print("测试报告：{}".format(cm.REPORT_DIR))
    print("日志目录：{}".format(cm.log_file))
    print("config.ini配置文件：{}".format(cm.ini_file))

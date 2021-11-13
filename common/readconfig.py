#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from config.conf import cm
from utils.utils_config import Config


class ReadConfig:
    _rc = Config(cm.ini_file)

    @property
    def dev_url(self):
        return self._rc.get("environment", "dev_url")


ini = ReadConfig()
if __name__ == "__main__":
    print(ini.dev_url)

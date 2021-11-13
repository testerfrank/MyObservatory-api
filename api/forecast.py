#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from common.baseapi import BaseApi
from common.readconfig import ini
from config.conf import cm
from utils.utils_yaml import ReadYAML


class Forecast(BaseApi):
    def __init__(self):
        self.param["base_url"] = ini.dev_url
        self.data = ReadYAML(cm.API_DIR, "weather")

    def forecast_of_9_day(self):
        return self.send(self.data["9-days-forecast"])

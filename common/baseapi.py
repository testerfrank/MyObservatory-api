#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json

import requests
import urllib3

from utils.utils_logger import log


class BaseApi:
    param = {}

    def send(self, data):
        urllib3.disable_warnings()
        raw_data = json.dumps(data)
        for key, value in self.param.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        log.info(f"请求数据：{data}")
        r = requests.request(**data, verify=False).json()
        log.info(f"响应报文：{r}")
        return r

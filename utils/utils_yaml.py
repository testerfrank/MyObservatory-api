#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

import yaml

from config.conf import cm


class ReadYAML:

    def __init__(self, dirname, filename):
        self.file = os.path.join(dirname, f"{filename}.yaml")
        if not os.path.exists(self.file):
            raise FileNotFoundError(f"{dirname}中不存在{filename}.yaml文件！")
        with open(self.file, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        data = self.data.get(item)
        return data

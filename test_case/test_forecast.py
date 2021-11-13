#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from api.forecast import Forecast


class TestForecast:
    def test_forecast(self):
        r = Forecast().forecast_of_9_day()
        min_rh = r["forecast_detail"][1]["min_rh"]
        max_rh = r["forecast_detail"][1]["max_rh"]
        print("the day after tomorrow's relative humidity is {}-{}%".format(min_rh, max_rh))

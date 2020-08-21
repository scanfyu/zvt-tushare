#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''=================================================
@Project :zvt-tushare
@FileName:tushare_kdata_recoder.py
@Python  :Python 3.5+
@Author  :Sunny
@Time    :2020/8/21/0021 11:19
@Desc    :
=================================================='''

import tushare as ts
import pandas as pd

from zvt.api import get_kdata, AdjustType
from zvt.api.quote import generate_kdata_id, get_kdata_schema, StockKdataCommon, Stock
from zvt.contract import IntervalLevel
from zvt.contract.api import df_to_db
from zvt.contract.recorder import FixedCycleDataRecorder
from zvt.domain import register_schema, declarative_base

from zvt_tm.domain import Stock1dKdata
from zvt_tm.recorders.baostock.common import to_bs_trading_level, to_bs_entity_id
from zvt.utils.pd_utils import pd_is_not_null
from zvt.utils.time_utils import to_time_str, TIME_FORMAT_DAY, TIME_FORMAT_ISO8601

class TuKdataRecoder(FixedCycleDataRecorder):
    pass

if __name__ == "__main__":
    pass

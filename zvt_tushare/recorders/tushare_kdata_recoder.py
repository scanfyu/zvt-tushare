#!/usr/bin/env python
# -*- coding:utf-8 -*-
import tushare as ts
import pandas as pd

from zvt.api import get_kdata, AdjustType
from zvt.api.quote import generate_kdata_id, get_kdata_schema, StockKdataCommon, Stock
from zvt.contract import IntervalLevel
from zvt.contract.api import df_to_db
from zvt.contract.recorder import FixedCycleDataRecorder
from zvt.domain import register_schema, declarative_base

from zvt.utils.pd_utils import pd_is_not_null
from zvt.utils.time_utils import to_time_str, TIME_FORMAT_DAY, TIME_FORMAT_ISO8601

class TuKdataRecoder(FixedCycleDataRecorder):
    provider = 'tushare'

    entity_provider = 'tushare'
    entity_schema = Stock

    # 将Provider注册到data_schema
    data_schema = StockKdataCommon

    def __init__(self,
                exchanges=['sh', 'sz'],
                entity_id=None,
                codes=None,
                batch_size=10,
                force_update=True,
                sleeping_time=1,
                default_size=2000,
                real_time=False,
                fix_duplicate_way='ignore',
                start_timestamp=None,
                end_timestamp=None,
                level=IntervalLevel.LEVEL_1DAY,
                kdata_use_begin_time=True,
                close_hour=None,
                close_minute=None,
                one_day_trading_minutes=24 * 60) -> None:
        level = IntervalLevel(level)
        self.data_schema = get_kdata_schema(entity_type='stock', level=level)



__all__ = ['TuKdataRecoder']

if __name__ == "__main__":
    pass

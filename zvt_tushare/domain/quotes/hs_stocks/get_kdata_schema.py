#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''=================================================
@Project :zvt-tushare
@FileName:get_kdata_scheme
@Python  :Python 3.5+
@Author  :Sunny
@Time    :2020/8/21/0021 13:23
@Desc    :
=================================================='''
from zvt.contract import IntervalLevel
from zvt.domain.quotes.gen_kdata_schema import gen_kdata_schema

if __name__ == '__main__':
    gen_kdata_schema(pkg='zvt_tushare', providers=['tushare'], entity_type='stock',
                     levels=[level for level in IntervalLevel])

if __name__ == "__main__":
    pass

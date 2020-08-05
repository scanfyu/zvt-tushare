# -*- coding: utf-8 -*-
from zvt.contract.register import register_schema
from zvt.domain.meta.stock_meta import StockMetaBase

from zvt.domain import Stock


def test_add_tushare_provider():
    register_schema(providers=['tushare'], db_name='stock_meta',
                    schema_base=StockMetaBase)

    Stock.query_data(provider='tushare')
    try:
        Stock.record_data(provider='tushare')
        assert False
    except Exception as e:
        print(e)
        
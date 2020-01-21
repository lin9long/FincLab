#!/usr/bin/python
# -*-coding:utf-8 -*-
from rest_framework import serializers
from .models import FincRBuySellD

class FincRBuySellDSerializer(serializers.ModelSerializer):
   # ModelSerializer和Django中ModelForm功能相似
   # Serializer和Django中Form功能相似
   class Meta:
       model = FincRBuySellD
       # 和"__all__"等价
       fields = ('id','ts_code','name','buy_price_finial','industry','diff_close','low','high','close','diff_lg_elg_amount','roll_return_flag','back_test_win_flag','buy_price_3','buy_price_5','back_test_win_gmean','back_test_win_label','buy_price','dt')
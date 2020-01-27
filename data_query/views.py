from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
# Create your views here.
from rest_framework.decorators import api_view

from .models import FincRBuySellD
from .serializers import FincRBuySellDSerializer
import json
# Create your views here.

def index(request):
    test_data = FincRBuySellD.objects.all()
    serializer = FincRBuySellDSerializer(test_data, many=True)
    return HttpResponse(serializer.data)

@api_view(['GET', 'POST'])
def get_data_by_dt(request):
    if request.method == 'GET':
        # ts_code = request.GET['ts_code']
        dt = request.GET['dt']
        try:
            search_kw = request.GET['search_kw']
        except:
            search_kw = ""
        if dt is not None:
            data = FincRBuySellD.objects.filter(dt__contains = dt)
            if search_kw is not "":
                data = data.filter(ts_code__contains = search_kw)
            serializer = FincRBuySellDSerializer(data, many=True)
            sd = serializer.data
            data_dict = {}
            data_dict['total'] = len(sd)
            data_dict['totalNotFiltered'] = len(sd)
            data_dict['rows'] = sd
            sd_js = json.dumps(data_dict,ensure_ascii=True)
            return HttpResponse(sd_js,content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('please set ts_code and dt')

@api_view(['GET', 'POST'])
def get_data_by_code(request):
    if request.method == 'GET':
        ts_code = request.GET['ts_code']
        dt = request.GET['dt']
        if ts_code is not None:
            data = FincRBuySellD.objects.filter(ts_code=ts_code).filter(dt=dt)
            serializer = FincRBuySellDSerializer(data, many=True)
            # jd = json.loads(serializer.data)
            sd = serializer.data[0]
            # del sd['name']
            # del sd['industry']
            data_dict = {}
            data_dict['total'] = 1
            data_dict['totalNotFiltered'] = 1
            data_dict['rows'] = [sd]
            sd_js = json.dumps(data_dict,ensure_ascii=True)
            return HttpResponse(sd_js,content_type="application/json,charset=utf-8")
        else:
            return HttpResponse('please set ts_code and dt')

# def index(request):
#    return HttpResponse(u"你好")
from django.http import HttpResponse
from django.shortcuts import render
from requests import Response
# Create your views here.
from rest_framework.decorators import api_view

import json
# Create your views here.


def bootstrapTable(request):
    return render(request,'bootstrapTable/index.html')

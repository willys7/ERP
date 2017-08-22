# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from serializers import *
from rest_framework import status
from rest_framework import serializers
from django.utils.six import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from service import AddUser

# Create your views here.
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'POST':
        data = JSONRenderer().render(request.data)
        model_serializer = UserSerializer(data=data)
        stream = BytesIO(data)
        final_model = JSONParser().parse(stream)
        AddUser(final_model)
        return HttpResponse(status=204)


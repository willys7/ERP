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
from rest_framework.response import Response
from service import AddUser, ExtractCredentialsFromJson, ValidateUserCredentials
from send_queue import *
from django.core import serializers
from  TokenResponseModel import *
import json

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
        try:
            data = JSONRenderer().render(request.data)
            model_serializer = UserSerializer(data=data)
            stream = BytesIO(data)
            final_model = JSONParser().parse(stream)
            token = AddUser(final_model)
            serialized_token = json.dumps(token, default=lambda o: o.__dict__)
            return Response(serialized_token, status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            stream = BytesIO(data)
            credentials = JSONParser().parse(stream)
            user_name, password = ExtractCredentialsFromJson(credentials)
            token = ValidateUserCredentials(user_name, password)
            serialized_token = json.dumps(token, default=lambda o: o.__dict__)
            return Response(serialized_token, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"err":str(e)}, status=status.HTTP_202_ACCEPTED)

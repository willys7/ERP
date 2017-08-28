# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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
from service import *
from django.core import serializers
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
def create_store(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            model_serializer = StoreSerializer(data=data)
            stream = BytesIO(data)
            store_model = JSONParser().parse(stream)
            store = AddNewStore(store_model)
            serialized_obj = serializers.serialize('json', [ store, ])
            return Response(serialized_obj, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def create_ingredient(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            stream = BytesIO(data)
            ingredient_model = JSONParser().parse(stream)
            ingredient = AddNewIngredient(ingredient_model)
            serialized_obj = serializers.serialize('json', [ ingredient, ])
            return Response(serialized_obj, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
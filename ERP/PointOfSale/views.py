# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
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


@csrf_exempt
@api_view(['GET', 'POST'])
def create_product(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            stream = BytesIO(data)
            product_model = JSONParser().parse(stream)
            print product_model
            product = CreateNewProduct(product_model)
            serialized_obj = serializers.serialize('json', [ product, ])
            return Response(serialized_obj, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def create_buyer(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            stream = BytesIO(data)
            buyer_model = JSONParser().parse(stream)
            print buyer_model
            buyer = CreateNewBuyer(buyer_model)
            serialized_obj = serializers.serialize('json', [ buyer, ])
            return Response(serialized_obj, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def create_recipe(request):
    if request.method == 'POST':
        try:
            data = JSONRenderer().render(request.data)
            stream = BytesIO(data)
            recipe_model = JSONParser().parse(stream)
            print recipe_model
            recipe = CreateNewRecipe(recipe_model)
            serialized_obj = serializers.serialize('json', [ recipe, ])
            return Response(serialized_obj, status=status.HTTP_202_ACCEPTED)
        except Exception, e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
from django.conf.urls import url
from PointOfSale import views

urlpatterns = [
    url(r'^api-pointofsale/product/$', views.create_product),
    url(r'^api-pointofsale/buyer/$', views.create_buyer),
]
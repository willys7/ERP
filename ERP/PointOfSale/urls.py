from django.conf.urls import url
from PointOfSale import views

urlpatterns = [
    url(r'^api-pointofsale/product/$', views.create_product),
    url(r'^api-pointofsale/buyer/$', views.create_buyer),
    url(r'^api-pointofsale/recipe/$', views.create_recipe),
    url(r'^api-purchases/invoice/$', views.create_invoice),
]
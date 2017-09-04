from django.conf.urls import url
from Purchases import views

urlpatterns = [
    url(r'^api-purchases/provider/$', views.create_provider),
    url(r'^api-purchases/purchase/$', views.process_purchase),
    
]
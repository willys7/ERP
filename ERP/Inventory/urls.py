from django.conf.urls import url
from Inventory import views

urlpatterns = [
    url(r'^api-inventory/store/$', views.create_store),
    url(r'^api-inventory/ingredient/$', views.create_ingredient),
]
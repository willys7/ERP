from django.conf.urls import url
from Inventory import views

urlpatterns = [
    url(r'^api-inventory/store/$', views.create_store),
    url(r'^api-inventory/ingredient/$', views.create_ingredient),
    url(r'^api-inventory/transaction/$', views.create_transaction),
    url(r'^api-inventory/validateingredient/$', views.validate_ingredient),
    
]
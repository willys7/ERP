from django.conf.urls import url
from Authentication import views

urlpatterns = [
    url(r'^api-auth/$', views.create_user),
]
from django.conf.urls import url
from Authentication import views

urlpatterns = [
    url(r'^api-auth/user/$', views.create_user),
    url(r'^api-auth/login/$', views.login),
]
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from parser_gps import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    ]
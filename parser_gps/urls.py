from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from parser_gps import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    url(r'^media/(?P<filename>[-\w]+)/table$', views.file_content, name='file_content'),
    ]
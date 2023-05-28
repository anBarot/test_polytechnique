from django.urls import path

from . import views

app_name = 'notion_home'

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('getdata', views.CrawlerView.getURLData, name='getURLData'),
]
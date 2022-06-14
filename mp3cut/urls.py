from django.urls import path
from . import views

app_name = 'mp3cut'
urlpatterns = [
    path('', views.index, name='index'),
    path('cutter/', views.mp3cut, name='mp3cut'),
]
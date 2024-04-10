from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('streaming/', views.streaming, name='streaming'),
    path('sharing/', views.sharing, name='sharing'),
]
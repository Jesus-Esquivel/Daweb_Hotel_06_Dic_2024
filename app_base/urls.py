from django.urls import path
from app_base import views
urlpatterns = [
    path("",views.index,name='index'),
]
from django.urls import path

from . import views

app_name = 'english'
urlpatterns = [
    path('', views.index, name='index'),
]

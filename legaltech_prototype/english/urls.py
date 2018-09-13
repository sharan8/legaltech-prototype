from django.urls import path

from . import views

app_name = 'english'
urlpatterns = [
    path('', views.index, name='index'),
    path('coa_view/', views.coa_view, name='coa_view'),
    path('coa_view/next/<int:paths_id>/', views.next, name='next')
]

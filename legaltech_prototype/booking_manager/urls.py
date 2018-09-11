from django.urls import path

from . import views

app_name = 'booking_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:session_id>/book/', views.book, name='book'),
]

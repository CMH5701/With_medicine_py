from django.urls import path
from with_medicine_app import views  

urlpatterns = [
    path('', views.main, name='main'),
    path('main_search/', views.main_search, name='main_search'),
]
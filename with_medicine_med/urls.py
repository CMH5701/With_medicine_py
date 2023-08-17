from django.urls import path
from with_medicine_med import views  

urlpatterns = [
    path('medicines/', views.medicines, name='medicines'), 
]
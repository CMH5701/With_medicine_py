from django.urls import path
from with_medicine_specialist import views  

urlpatterns = [
    path('specialist/', views.specialist, name='specialist'), 
]
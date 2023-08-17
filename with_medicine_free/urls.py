from django.urls import path
from with_medicine_free import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('free_read/', views.free_read, name='free_read'),
    path('free_create/', views.free_create, name = 'free_create'),
    path('free_read/', views.free_read, name = 'free_read'),
    path('free_detail/<str:id>/', views.free_detail, name= 'free_detail'),
    path('free_update/<str:id>/', views.free_update, name = 'free_update'),
    path('free_delete/<str:id>/', views.free_delete, name='free_delete'),
    path('<int:id>/comments/<int:c_id>/free_comment_delete', views.free_comment_delete, name="free_comment_delete"),
    path('free_comment_update/<int:id>/<int:com_id>/', views.free_comment_update, name="free_comment_update"),
    path('free_search/', views.free_search, name='free_search'),
    path('<int:id>/free_like/', views.free_like, name='free_like'), 
]
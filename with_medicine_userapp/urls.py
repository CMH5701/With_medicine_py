from django.urls import path 
from with_medicine_userapp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>', views.user_detail, name='user_detail'),
    path('user_update/', views.user_update, name='user_update'),
    path('user_delete/', views.user_delete, name='user_delete'),
    path('password/', views.change_password, name='change_password'),
    path('user_detail', views.user_detail, name='user_detail'), 
    path('signup_welcome/', views.signup_welcome, name='signup_welcome'),
    path('my_posts/', views.my_posts, name='my_posts'),
    path('my_health/', views.my_health, name='my_health'),
]

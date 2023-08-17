from django.urls import path
from with_medicine_review import views  

urlpatterns = [
    path('review_read/', views.review_read, name='review_read'),
    path('review_create/', views.review_create, name = 'review_create'),
    path('review_detail/<str:id>/', views.review_detail, name= 'review_detail'),
    path('review_update/<str:id>/', views.review_update, name = 'review_update'),
    path('review_delete/<str:id>/', views.review_delete, name='review_delete'),
    path('<int:id>/comments/<int:c_id>/review_comment_delete', views.review_comment_delete, name="review_comment_delete"),
    path('review_comment_update/<int:id>/<int:com_id>/', views.review_comment_update, name="review_comment_update"),
    path('search/', views.search, name = 'search'),
    path('<int:id>/review_like/', views.review_like, name='review_like'), 
]
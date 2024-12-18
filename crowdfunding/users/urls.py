from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('users/<int:pk>/projects/', views.UserProjects.as_view()),  
    path('users/<int:pk>/pledges/', views.UserPledges.as_view()), 
     path('users/public/<int:pk>/', views.PublicUserDetail.as_view(), name='public-user-detail'),
    ]
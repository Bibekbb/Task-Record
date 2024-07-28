from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.Register, name='register'),
    path('login/', views.Login_User, name='login'),
    path('logout/', views.Logoutuser, name = 'logout' ),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('create-record/', views.Create_record, name='create-record'),
    path('update-recrod/<int:pk>/', views.UpdateRecord, name='record-update'),
    path('view-record/<int:pk>/', views.view_record, name='view-record'),
    path('delete-record/<int:pk>/', views.Delete_record, name='delete-rec'),
]

from django.urls import path
from . import views
app_name= 'accounts'

urlpatterns=[
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('delete/', views.DeleteView, name='delete'),
    path('logout/', views.LogoutView, name='logout'),
]
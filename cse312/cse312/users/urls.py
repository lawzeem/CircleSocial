from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('signup/', views.CreateAccountView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
]
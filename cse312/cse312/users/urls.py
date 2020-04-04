from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('signup/', views.CreateAccountView.as_view(), name='signup'),
    path('login/', views.LogInView.as_view(), name='login'),
    # path('', showLogin, name='showLogin'),
    # path('signup', showSignup, name='showSignup'),
]
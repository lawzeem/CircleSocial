from .views import showNotifications, editNotifications
from django.urls import path

app_name = 'notifications'

urlpatterns = [
    path('', showNotifications, name='showNotifications'),
    path('<slug:operation>/<slug:messageID>', editNotifications, name='editNotifications')
]
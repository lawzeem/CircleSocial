from .views import InboxView, ThreadView, GetThread
from django.urls import path

app_name = 'message'

urlpatterns = [
    # path('', InboxView.as_view(), name='viewMessage'),
    # path('<slug:username>', ThreadView.as_view(), name='viewMessage')
    path('<slug:username>', GetThread, name='showMessage')
    # path('message/<slug:username>', GetThread, name='showMessage')
]
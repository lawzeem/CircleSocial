from .views import InboxView, ThreadView, GetThread
from django.urls import path
from django.conf.urls import url

app_name = 'message'

urlpatterns = [
    # path('', InboxView.as_view(), name='viewMessage'),
    # path('<slug:username>', ThreadView.as_view(), name='viewMessage')
    url(r"^(?P<username>\w+)/", GetThread, name='showMessage')
    # path('message/<slug:username>', GetThread, name='showMessage')
]
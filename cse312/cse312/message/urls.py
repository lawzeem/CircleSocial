from .views import InboxView, ThreadView
from django.urls import path

app_name = 'message'

urlpatterns = [
    path('', InboxView.as_view(), name='showMessage'),
    path('<slug:operation>/<slug:username>', ThreadView.as_view(), name='showThread')
]
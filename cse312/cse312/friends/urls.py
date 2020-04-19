from .views import showFriends, editFriends
from django.urls import path

app_name = 'friends'

urlpatterns = [
    path('', showFriends, name='showFriends'),
    path('<slug:operation>/<slug:username>', editFriends, name='editFriends')
]
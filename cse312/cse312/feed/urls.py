from .views import showFeed
from django.urls import path

urlpatterns = [
    path('', showFeed, name='showFeed'),
]
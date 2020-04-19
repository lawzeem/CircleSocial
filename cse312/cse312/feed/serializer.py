from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

from .models import Post, Comments

class CommentSerializer(serializers.ModelSerializer):
    

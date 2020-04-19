from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from rest_framework import serializers

from .models import Post, Comments
from cse312.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    upvotes = UserSerializer(many=True)
    class Meta:
        model = Post
        fields = ('title', 'image', 'description', 'upvotes', 'user')


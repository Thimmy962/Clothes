from rest_framework import serializers, response, status
from .models import Profile, User
from django.db import IntegrityError

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def create(self, cd):
        user = User.objects.create_user(username=cd['username'].lower(),
            email=cd['email'], password=cd['password'])
        user.save()
        return user
from rest_framework import serializers
from graphql_jwt.utils import jwt_payload, jwt_encode

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # sending back token for initial login
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        # generate new token
        return jwt_encode(jwt_payload(obj))

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
        
    class Meta:
        model = User
        fields = ["password", "username", "email", "token"]
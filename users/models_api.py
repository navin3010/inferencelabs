from django.contrib import auth
from django.core import exceptions
from rest_framework import serializers, response
from django.contrib.auth import authenticate

User = auth.get_user_model()

class UserManagementModel:

    def is_valid_user(self, username: str, password: str, is_active=True):
        try:
            user_data = User.objects.get(username = username, is_active = is_active)
        except exceptions.ObjectDoesNotExist:
            print("wrong user name")
            raise serializers.ValidationError({
                "result": False,
                "msg": "Invalid Username or Mobile Number"},
                code="validation_error",
            )
        # print("user_daa", user_data.password)
        user_matched = authenticate(username=username, password=password)
        if not user_matched:
            raise serializers.ValidationError({
                "result": False,
                "msg": "Invalid Username or Password"},
            )
        return user_data
    
    def get_user_data_by_username(self, username: str):
        user_data = User.objects.get(username = username, is_active=True)
        if not user_data:
            raise serializers.ValidationError({
                "result": False,
                "msg": "Inactive Username"},
            )
        return user_data

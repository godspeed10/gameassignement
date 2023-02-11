from django.contrib.auth import get_user_model
# User = get_user_model() 


from rest_framework import serializers
from .models import *


class Player(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'username', 'email', 'password','created_at']
    #     extra_kwargs = {
    #         'password': {'write_only': True}
    #     }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# class EmployeeUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         fields = ['username', 'email' , 'phone' ]

from django.contrib.auth import get_user_model
# User = get_user_model() 


from rest_framework import serializers
from .models import *


class GameSerailizer(serializers.ModelSerializer):
    new_string = serializers.CharField(max_length=6,default="", allow_blank=True)
    class Meta:
        model = Game
        fields = ['id','game_id', 'new_string']
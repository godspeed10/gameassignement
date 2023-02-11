from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from authentication.models import UserAccount
from rest_framework.response import Response
from collections import Counter
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import parsers    
from .serializers import *


class StartGame(APIView):
    def post(self, request):
        user = request.user.id
        request_data = request.data
        request_data['game_id'] = user
        serializer = GameSerailizer(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)

import random
class UpdateBoard(APIView):
    def patch(self,request):
        user = request.user.id
        request_data = request.data
        new_id = request_data['id']                                ### Taking the id in user input , so can filter out specifc entered by user
        new_data = request_data['new_string']
        charLen =  Game.objects.filter(id=new_id).values_list('new_string')[0][0]
        list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        random_char = random.choice(list1)

        if len(charLen) == 6:                                       ## Checking if len of new_String is 6
            if charLen == charLen[::-1]:                 ## Checking if reverse and original are same or not
                return Response({
                    "Hurray":f"{charLen},is a paldindrome"
                })
            else:
                return Response('Not a Palindrome')                                  
        else:
            new_data_string = charLen + new_data + random_char                              ## Getting oldstring + new_string + random character 
            patch_data = Game.objects.filter(id=new_id).update(new_string=new_data_string)   ## Now passing the REQUESTED ID  id to filter and  to update the specific string of the user
            game_data = Game.objects.filter(id=new_id).values()                              ## Filtered out data which was updated to show in response
            return Response(game_data,status=status.HTTP_201_CREATED)
    
    def get(self,request):
        user = request.user.id
        game_data = Game.objects.filter(game_id=user).values()   ## Getting Gamedata and ID's of specific user , game _id
        return Response(game_data)



class ListofGamedata(APIView):
    def get(self,request):
        user = request.user.id
        game_data = Game.objects.all().values()   ## Getting Gamedata and ID's of all users
        return Response(game_data)
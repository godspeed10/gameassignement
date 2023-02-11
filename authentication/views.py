from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import *
from .models import *

class PlayerRegister(APIView):
    def post(self, request):
        request_data = request.data
        serializer = Player(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)


class RetrieveUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = request.user
    print(user)
    # u = UserAccount.objects.filter(id=user).values_list('role')[0][0]
    # print(u)
    # if u == "Customer":
    user = Player(user)

    return Response(user.data, status=status.HTTP_200_OK)

class RetrieveUserView(APIView):
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    user = request.user
    print(user)
    # u = UserAccount.objects.filter(id=user).values_list('role')[0][0]
    # print(u)
    # if u == "Customer":
    user = EmployeeUserSerializer(user)

    return Response(user.data, status=status.HTTP_200_OK)


# class Role(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         user_id = request.user.id
#         print(user_id,'user id')
#         # request.data['customer_id'] = user_id
#         t = UserAccount.objects.filter(id=user_id).values_list('role')[0][0]
#         return Response(t)
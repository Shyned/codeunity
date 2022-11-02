from django.shortcuts import render
# 
from user.serializer import UserSerializer
# 
from .models import UserModel
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(["GET"])
def get_user(request,pk):
    user = UserModel.objects.get(pk = pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


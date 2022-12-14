from msilib.schema import SelfReg
from rest_framework import serializers
from .models import ChatroomModel   



class ChatroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatroomModel
        fields = [ 'room_creator', 'guest','name',]
        depth = 1
        
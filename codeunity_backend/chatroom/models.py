from unittest.util import _MAX_LENGTH
from django.db import models
from user.models import UserModel

class ChatroomModel(models.Model):
    room_creator = models.ForeignKey(UserModel, on_delete = models.CASCADE, related_name='creator')
    guest = models.ForeignKey(UserModel, on_delete = models.CASCADE, related_name='guest',blank= True)
    name = models.CharField(max_length = 20, default= "Chatroom" )
    depth= 1
        
    
from django.db import models
from authentication.models import UserAccount
# Create your models here.

class Game(models.Model):
    game_id = models.ForeignKey(UserAccount,on_delete=models.CASCADE,default="")
    new_string = models.CharField(max_length=6,default="")

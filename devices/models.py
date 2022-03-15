from cmd import IDENTCHARS
from pyexpat import model
from sre_parse import State
from unittest.mock import create_autospec
from django.db import models
from uuid import uuid4
# Create your models here.

class Devices(models.Model):

    id_device = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    title = models.CharField(max_length=255)
    create_at = models.DateField(auto_now_add=True)
    state = models.BooleanField(default=True)
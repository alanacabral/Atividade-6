from django.db import models
from django.utils import timezone

class Pessoa (models.Model):
  name = models.CharField(max_length= 20)
  lastname = models.CharField(max_length= 50)
  nascimento = models.DateField(default=timezone.now)
  email = models.EmailField(default = "")
  

class AssistirCorrida (models.Model):
  local = models.CharField(max_length= 50)
  due_date = models.DateField(default = timezone.now)
  duracao = models.IntegerField(default = 0)
  done = models.BooleanField(default = False)
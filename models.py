#No models é onde estão as classes, que contém as informações sobre os dados do app. Dadas as informações fornecidas pelo models, ocorre a realização das migrações 
#makemigrations que é o sistema que empacota as alterações feitas no models e migram elas para o resto do programa e migrate que é o sistema para aplicar as migrações 
#guardadas no makemigrations no banco de dados.


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

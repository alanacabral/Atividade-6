#Através do arquivo admin é possível que as classes criadas em models apareçam no admin do app

from django.contrib import admin
from .models import Pessoa
from .models import AssistirCorrida

admin.site.register(Pessoa)
admin.site.register(AssistirCorrida)

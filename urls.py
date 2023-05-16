#O arquivo url permite que uma nova url seja criada para a página principal, ambos os forms, edição dos forms e exclusão dos forms.

"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appdalexinha import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = 'principal'),
    path('form1',views.form1),
    path('form2',views.form2),
    path('Pessoa/edit/<usuario_id>', views.update_form1),
    path('Pessoa/delete/<usuario_id>', views.delete_form1),
    path('Corrida/edit/<cadacorrida_id>', views.update_form2),
    path('Corrida/delete/<cadacorrida_id>', views.delete_form2)
]


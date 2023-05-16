# Atividade-6

No arquivo README.md, adicionar o passo a passo referente à configuração do Django (tudo que rodaram na linha de comando desde a primeira atividade);


python
import secrets
secrets.token_urlsafe(32)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

views:

Na página views é o local dentro do app que possui todas as funções necessárias para renderizar os templates, ou seja, as funções dentro do views puxam os objetos das classes do banco de dados para um html tendo um contexto, que é o dicionário em que as chaves foram atribuídas ao conjunto de objetos.

models:

No models é onde estão as classes, que contém as informações sobre os dados do app. Dadas as informações fornecidas pelo models, ocorre a realização das migrações makemigrations que é o sistema que empacota as alterações feitas no models e migram elas para o resto do programa e migrate que é o sistema para aplicar as migrações guardadas no makemigrations no banco de dados.

admin:

Através do arquivo admin é possível que as classes criadas em models apareçam no admin do app

url:

O arquivo url permite que uma nova url seja criada para a página principal, ambos os forms, edição dos forms e exclusão dos forms.


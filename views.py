from django.shortcuts import render 
from .models import Pessoa
from .models import AssistirCorrida
from django.shortcuts import render, redirect

def home(request):
  list = Pessoa.objects.all()
  list2 = AssistirCorrida.objects.all()
  context = {'Pessoa':list,'Corrida':list2}
  return render(request, "home.html",context = context)

  
def form1 (request):
  if request.method=='POST':
    print(request.POST)
    Pessoa.objects.create(
      name = request.POST['nome'],
      lastname = request.POST['sobrenome'],
      nascimento=request.POST['nascimento'],
      email = request.POST['email']
    )
    return redirect('principal')
  return render(request,'form1.html')

def form2 (request):
  if request.method=='POST':
    print(request.POST)
    AssistirCorrida.objects.create(
      local=request.POST['local'],
      due_date = request.POST['due-date'],
      duracao=request.POST['duracao'],
      done=False
    )
    return redirect('principal')
  return render(request,'form2.html')

def update_form1 (request, usuario_id):
  usuario = Pessoa.objects.get(id = usuario_id )
  usuario.nascimento = usuario.nascimento.strftime('%Y-%m-%d')
  if request.method == "POST":
    usuario.name = request.POST['nome'],
    usuario.lastname = request.POST['sobrenome'],
    usuario.nascimento = request.POST['nascimento'],
    usuario.email = request.POST['email']
    usuario.save() 
    return redirect("principal") 
  return render(request, "form1.html", context={"usuario": usuario})

def update_form2 (request, cadacorrida_id):
  cadacorrida = AssistirCorrida.objects.get(id = cadacorrida_id )
  cadacorrida.due_date = cadacorrida.due_date.strftime('%Y-%m-%d')
  if request.method == "POST":
    cadacorrida.local = request.POST['local'],
    cadacorrida.due_date = request.POST['due-date'],
    cadacorrida.duracao = request.POST['duracao'],
    if "done" not in request.POST:
            cadacorrida.done = False
    else:
        cadacorrida.done = True
    cadacorrida.save()
    return redirect("principal") 
  return render(request, "form2.html", context={"cadacorrida": cadacorrida})

def delete_form1(request, usuario_id):
    usuario = Pessoa.objects.get(id=usuario_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        usuario.delete()

      return redirect("principal")

    return render(request, "deleteform1.html", context={"usuario": usuario})
    
def delete_form2(request, cadacorrida_id):
    cadacorrida = AssistirCorrida.objects.get(id=cadacorrida_id)
    if request.method == "POST":
      if "confirm" in request.POST:
        cadacorrida.delete()

      return redirect("principal")

    return render(request, "deleteform2.html", context={"cadacorrida": cadacorrida})


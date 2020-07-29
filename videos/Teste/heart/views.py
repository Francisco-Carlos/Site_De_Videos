from django.shortcuts import render, redirect
from heart.models import Videos,Perfil,Coment
from .forms import Creat_Video, Creat_user, Creat_Coment, Creat_Perfil
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Index(request):
    vid = Videos.objects.all()
    busca = request.GET.get('seacher')
    if busca:
        vid = Videos.objects.filter(Categoria=busca )
    if request.POST:
        coment = Creat_Coment(request.POST)
        if coment.is_valid():
            coment.save()
            return redirect('/')
    else:
        comentario= Creat_Coment()
    context = {'vid':vid,'comentario':comentario}
    return render(request,'index.html',context)

@login_required(login_url='/heart/login/')
def Usuario(request):
    vid = Videos.objects.all()
    use = User.objects.all()
    per = Perfil.objects.all()
    context = {'vid':vid,'use':use,'per':per}
    return render(request,'Usuario.html',context)


def Detalhes(request,id):
    vid = Videos.objects.get(id=id)
    com = Coment.objects.filter(video=vid)
    per = Perfil.objects.all()
    context = {'vid':vid,'com':com,'per':per}
    return render(request,'Detalhes.html',context)

@login_required(login_url='/heart/login/')
def Cadastrar(request):
    if request.method =='POST':
        vid = Creat_Video(request.POST,request.FILES)
        if vid.is_valid():
            vid.save()
            return redirect('/')
    else:
        vid =Creat_Video()
    return render(request,'Cadastrar.html',{'vid':vid})

# cadastrar Usuarios
def Cadastrar_User(request):
    if request.POST:
        usuarios = Creat_user(request.POST,request.FILES)
        if usuarios.is_valid():
            usuarios.save()
            return redirect('/heart/usuario/')
    else:
        usuarios= Creat_user()
    return render(request,'Cadastrar_user.html',{'usuarios':usuarios})

# cadastrar perfil
@login_required(login_url='/heart/login/')
def Cadastar_perfil(request):
    per = Perfil.objects.all()
    if request.POST:
        perfil = Creat_Perfil(request.POST,request.FILES)
        if perfil.is_valid():
            perfil.save()
            return  redirect('/heart/usuario/')
    else:
        perfil = Creat_Perfil()
    context={'perfil':perfil,'per':per}
    return  render(request,'Cadastro_perfil.html',context)


# cadastrar comentario
@login_required(login_url='/heart/login/')
def Cadastrar_coment(request):
    if request.POST:
        coment = Creat_Coment(request.POST)
        if coment.is_valid():
            coment.save()
            return redirect('/heart/detalhes')
    else:
        comentario= Creat_Coment()
    return render(request,'index.html',{'comentario':comentario})

#login e logouf
def Login(request):
    return render(request,'login.html')

def Logout(request):
    return render(request,'login.html')
def Login_user(request):
    if request.POST:
        use = request.POST.get('username')
        pas = request.POST.get('password')
        user = authenticate(username=use,password=pas)
        if user is not None:
            login(request,user)
            return redirect('/heart/usuario/')
        else:
            messages.error(request,'usuario ou senha errado')
    return redirect('/heart/login')
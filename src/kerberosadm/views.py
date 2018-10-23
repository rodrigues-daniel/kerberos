from django.shortcuts import render
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth import authenticate,login
from django.core.exceptions import PermissionDenied

from django.db import connection
import datetime



def home(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    return render(request,"home.html")




def login(request):

    nomeUsuario = request.POST['username']
    senha       = request.POST['password']

    usuario     = authenticate(request,username=nomeUsuario,password=senha)
    if usuario is not None:
        login(request,usuario)
        return HttpResponse("Logado")

    else:
        return HttpResponse("Usuario Não Encontradao!")



def first_view(request):
    cursor = connection.cursor()
    try:
        #cursor.callproc('[dbo].[permissions_list]', ['', '', ''])
        cursor.execute("EXEC [dbo].[permissions_list] '%', '%', '%' ")
        if cursor.return_value == 1:
            result_set = cursor.fetchall()
    finally:
        cursor.close()
    return HttpResponse("primeira view")

def reg(request):
    return render(request, "main.html",{}) 


def notfound(request,foo=0):
    if foo:
        return HttpResponseNotFound('<h1>Pagina Encontrada!</h1>')
    else:
        return HttpResponse('<h1> Pagina Não Encontrada</h1>')


def pagina(request):
    return HttpResponse('<h2> Pagina Resposta </h2>')

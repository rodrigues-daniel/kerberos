from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render
from kerberosadm.models import Produto

from django.db import connection
import datetime




def index(request):

    try:
        p = Produto.objects.all()
    except Produto.DoesNotExist:

        raise Http404("Pagina Não Encontrada")

    return render(request,'kerberosadm/index.html',{'valores':p})



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



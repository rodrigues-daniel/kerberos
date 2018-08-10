from django.shortcuts import render
from django.http import HttpResponse

from django.db import connection


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

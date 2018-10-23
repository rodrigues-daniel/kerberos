from django.urls import path
from django.contrib import admin
from . import views

admin.site.site_header = 'Data Control Admin'
admin.site.site_title = 'Data Control Admin'
admin.site.index_title = 'Data Control Admin'

urlpatterns = [
    # ex: /polls/
    path('', views.home,name="home"),
    path('registro',views.login,name="login"),
    path('reg',views.reg,name="reg"),
    path('notfound/<int:foo>',views.notfound,name="notfound")
    path('pagina',views.pagina,name="pagina")
    # ex: /polls/5/
    ]

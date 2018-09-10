from django.contrib import admin
from django import *
from .models import *
from .filters import *

# Register your models here.

class KerberosAdminSite(admin.AdminSite):
    site_header = 'Data Control Administration'
    index_title = "Visualizções"

admin_site = KerberosAdminSite(name="dcadmin")



class GrupoAdmin(admin.ModelAdmin):
    fields = ("nomegrupo","ativo")
    list_display = ("nomegrupo","ativo",)
    list_filter = ('nomegrupo','ativo',)
    search_fields = ['nomegrupo']

admin_site.register(Grupo,GrupoAdmin)


    #readonly_fields = ["datainclusao","usuarioinclusao"]


class ProdutoAdmin(admin.ModelAdmin):
    pass
    #readonly_fields = ["datainclusao","usuarioinclusao"]
admin_site.register(Produto,ProdutoAdmin)




class ProdutoGrupoAdmin(admin.ModelAdmin):

    list_display = ('idproduto', 'idgrupo',)
    list_filter = ('idproduto','idgrupo',)
    search_fields = ['idproduto__nomeproduto']

admin_site.register(Produtogrupo, ProdutoGrupoAdmin)
#class PrudutoProjetoAdmin(admin.ModelAdmin):
#    list_display = ('idproduto', 'idprojeto',)
#    list_filter = ('idproduto','idprojeto')
#    search_fields = ['idproduto']
    #readonly_fields = ["datainclusao","usuarioinclusao"]


class  ProdutoSysDatabaseAdmin(admin.ModelAdmin):
    list_display = ('idproduto', 'database_name',)
    list_filter = ('idproduto','database_name')
    search_fields = ['idproduto__nomeproduto']
admin_site.register(Produtosysdatabase,ProdutoSysDatabaseAdmin)

#@admin.register(Projeto)
#class  ProjetoAdmin(admin.ModelAdmin):
#    pass
    #readonly_fields = ["datainclusao","usuarioinclusao"]



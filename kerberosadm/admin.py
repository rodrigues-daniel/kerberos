from django.contrib import admin
from django import *
from .models import *
from .filters import *

# Register your models here.

class KerberosAdminSite(admin.AdminSite):
    site_header = 'Monty Python administration'

admin_site = KerberosAdminSite(name="dcadmin")



class GrupoAdmin(admin.ModelAdmin):
    fields = ("nomegrupo","ativo")
    list_display = ("nomegrupo","ativo",)
    list_filter = ('nomegrupo','ativo',)
    search_fields = ['nomegrupo']

admin_site.register(Grupo,GrupoAdmin)


    #readonly_fields = ["datainclusao","usuarioinclusao"]

@admin.register(Produto)
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

class  UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nomeusuario', 'loginusuario')
    search_fields = ['loginusuario','nomeusuario']
    #readonly_fields = ["datainclusao","usuarioinclusao"]
admin_site.register(Usuario,UsuarioAdmin)


class  UsuariogrupoAdmin(admin.ModelAdmin):
    list_display = ('idusuario','idgrupo',)
    list_filter = ('idusuario','idgrupo',)
    search_fields = ['idusuario__nomeusuario']
    #readonly_fields = ["datainclusao","usuarioinclusao"]
admin_site.register(Usuariogrupo,UsuariogrupoAdmin)


class  UsuarioprodutoAdmin(admin.ModelAdmin):
    list_display = ('idusuario','idproduto',)
    list_filter = ('idusuario','idproduto',)
    search_fields = ['idusuario__nomeusuario']
admin_site.register(Usuarioproduto,UsuarioprodutoAdmin)


@admin.register(Permissoeslist)
class  PermissoeslistAdmin(admin.ModelAdmin):
    list_display = ('ambiente','permissionlevel','dbname','grupo','produto','usuario',)
    list_filter = (
              ('ambiente',DropdownFilter)
            , ('permissionlevel',DropdownFilter)
            , ('dbname',DropdownFilter)
            , ('grupo',DropdownFilter)
            , ('produto',DropdownFilter)
            , ('usuario',DropdownFilter),)

    search_fields = ['ambiente','permissionlevel','dbname','grupo','produto','usuario']
    readonly_fields = ('lider','grupo','usuario', 'produto', 'dbname', 'typeoflogin', 'typeofrole', 'permissionlevel',)
    list_display_links = None

    fieldsets = (
        ('Perfil',{'fields':('usuario','typeofrole',)}),
        ('Opções Avançadas',{'classes':('collapse',),'fields':('dbname',)}),
    )

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    #def has_change_permission(self, request):
        #return False

    def has_delete_permission(self, request,obj=None):
       return False
admin_site.register(Permissoeslist, PermissoeslistAdmin)
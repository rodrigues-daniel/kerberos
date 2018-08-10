from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    fields = ("nomegrupo","ativo")
    list_display = ("nomegrupo","ativo",)
    list_filter = ('nomegrupo','ativo',)
    search_fields = ['nomegrupo']
    #readonly_fields = ["datainclusao","usuarioinclusao"]

@admin.register(Produto)
class PrudutoAdmin(admin.ModelAdmin):
    pass
    #readonly_fields = ["datainclusao","usuarioinclusao"]

@admin.register(Produtogrupo)
class PrudutoGrupoAdmin(admin.ModelAdmin):
    list_display = ('idproduto', 'idgrupo',)
    list_filter = ('idproduto','idgrupo',)
    search_fields = ['idproduto']
    #readonly_fields = ["datainclusao","usuarioinclusao"]

@admin.register(Produtoprojeto)
class PrudutoProjetoAdmin(admin.ModelAdmin):
    list_display = ('idproduto', 'idprojeto',)
    list_filter = ('idproduto','idprojeto')
    search_fields = ['idproduto']
    #readonly_fields = ["datainclusao","usuarioinclusao"]

@admin.register(Produtosysdatabase)
class  ProdutoSysDatabaseAdmin(admin.ModelAdmin):
    list_display = ('idproduto', 'database_name',)
    list_filter = ('idproduto','database_name')
    search_fields = ['idproduto']

@admin.register(Projeto)
class  ProjetoAdmin(admin.ModelAdmin):
    pass
    #readonly_fields = ["datainclusao","usuarioinclusao"]

@admin.register(Usuario)
class  UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nomeusuario', 'loginusuario')
    search_fields = ['loginusuario','nomeusuario']
    #readonly_fields = ["datainclusao","usuarioinclusao"]

@admin.register(Usuariogrupo)
class  UsuariogrupoAdmin(admin.ModelAdmin):
    list_display = ('idusuario','idgrupo',)
    list_filter = ('idusuario','idgrupo',)
    search_fields = ['idusuario']
    #readonly_fields = ["datainclusao","usuarioinclusao"]


@admin.register(Usuarioproduto)
class  UsuarioprodutoAdmin(admin.ModelAdmin):
    list_display = ('idusuario','idproduto',)
    list_filter = ('idusuario','idproduto',)
    search_fields = ['idusuario']


@admin.register(Permissoeslist)
class  PermissoeslistAdmin(admin.ModelAdmin):
    list_display = ('grupo','usuario', 'produto', 'dbname', 'typeoflogin', 'typeofrole', 'permissionlevel',)
    list_filter = ('grupo', 'produto','permissionlevel', 'usuario',)
    search_fields = ['usuario']
    readonly_fields = ('lider','grupo','usuario', 'produto', 'dbname', 'typeoflogin', 'typeofrole', 'permissionlevel',)
    fieldsets = (
        ('Perfil',{'fields':('usuario','typeofrole',)}),
        ('Opções Avançadas',{'classes':('collapse',),'fields':('dbname',)}),
    )

    def has_add_permission(self, request):
        return False

    #def has_change_permission(self, request):
        #return False

    def has_delete_permission(self, request,obj=None):
       return False

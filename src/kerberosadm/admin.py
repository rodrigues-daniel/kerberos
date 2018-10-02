from django.contrib import admin
from django import *
from .models import *
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.translation import gettext_lazy as _

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



#  Modificar ----
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




#  Modificar ----
class ProdutoGrupoAdmin2(admin.ModelAdmin):

    list_display = ('idp')
    #list_filter = ('idproduto','idgrupo',)
    #search_fields = ['idproduto__nomeproduto']
admin_site.register(ProdutogrupoTeste, ProdutoGrupoAdmin2)


class  ProdutoSysDatabaseAdmin(admin.ModelAdmin):
    list_display = ('idproduto', 'database_name',)
    list_filter = ('idproduto','database_name')
    search_fields = ['idproduto__nomeproduto']
admin_site.register(Produtosysdatabase,ProdutoSysDatabaseAdmin)

#@admin.register(Projeto)
#class  ProjetoAdmin(admin.ModelAdmin):
#    pass
    #readonly_fields = ["datainclusao","usuarioinclusao"]


# ------------------------------- FLAT PAGES -----------------------------------------



# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'enable_comments',
                'registration_required',
                'template_name',
            ),
        }),
    )

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

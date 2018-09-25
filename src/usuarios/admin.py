from django.contrib import admin
from usuarios.models import Usuario,Usuariogrupo,Usuarioproduto
from kerberosadm.admin import admin_site

# Register your models here.





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

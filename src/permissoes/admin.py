from django.contrib import admin
from .filters import *
from .models import *
from kerberosadm.admin import admin_site

# Register your models here.


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
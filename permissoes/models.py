from django.db import models

# Create your models here.




class Permissoeslist(models.Model):
    ambiente = models.CharField(db_column='ambiente', max_length=20)
    grupo = models.CharField(db_column='Grupo', max_length=50)
    usuario = models.CharField(db_column='usuario', max_length=50)
    lider = models.BooleanField()
    produto = models.CharField(db_column='produto', max_length=50)
    dbname  = models.CharField(db_column='dbname', max_length=50)
    typeoflogin  = models.CharField(db_column='typeoflogin', max_length=50)
    typeofrole = models.CharField(db_column='typeofrole', max_length=50)
    permissionlevel = models.CharField(db_column='permissionlevel', max_length=50)

    class Meta:
        managed = False
        db_table = 'Permissoes'
        verbose_name = 'Lista de Permissões'
        verbose_name_plural = 'Lista de Permissões'
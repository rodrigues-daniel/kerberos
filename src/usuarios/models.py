from django.db import models
from kerberosadm.models import Grupo,Produto



class Usuario(models.Model):
    idusuario = models.AutoField(db_column='IdUsuario', primary_key=True)  # Field name made lowercase.
    loginusuario = models.CharField("Login",db_column='LoginUsuario', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nomeusuario = models.CharField("Nome do Usuário",db_column='NomeUsuario', max_length=50)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.   


    def __str__(self):
        return self.nomeusuario


    class Meta:
        managed = False
        db_table = 'Usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nomeusuario',]
        
        
        
        

class Usuariogrupo(models.Model):
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='IdUsuario', primary_key=True, verbose_name='Usuário')  # Field name made lowercase.
    idgrupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='IdGrupo', verbose_name='Grupo')  # Field name made lowercase.
    #datainclusao = models.DateTimeField(db_column='DataInclusao')  # Field name made lowercase.
    #usuarioinclusao = models.CharField(db_column='UsuarioInclusao', max_length=20)  # Field name made lowercase.

    def __str__(self):
        return " %s - %s" % (self.idusuario, self.idgrupo)


    class Meta:
        managed = False
        db_table = 'UsuarioGrupo'
        unique_together = (('idusuario', 'idgrupo'),)
        verbose_name = 'Usuário Grupo - Vinculação'
        verbose_name_plural = 'Usuários Grupos - Vinculações'
        ordering = ['idusuario','idgrupo']


class Usuarioproduto(models.Model):
    id = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='IdUsuario', verbose_name='Usuário')  # Field name made lowercase.
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='IdProduto', verbose_name='Produto')  # Field name made lowercase.
    lider = models.BooleanField(db_column='Lider')  # Field name made lowercase.
    



    class Meta:
        managed = False
        db_table = 'UsuarioProduto'
        unique_together = (('idusuario', 'idproduto'),)
        verbose_name = 'Usuário Produto - Vinculação'
        verbose_name_plural = 'Usuários Produtos - Vinculações'





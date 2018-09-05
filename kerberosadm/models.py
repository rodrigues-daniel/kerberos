# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Usuario(models.Model):
    USUARIO_TIPO = (
        ('DOM', 'DOMINIO'),
        ('APP', 'APLICAÇÃO'),
        ('SERV', 'SERVIÇO'),
    )
    idusuario = models.AutoField(primary_key=True)  # Field name made lowercase.
    nomeusuario = models.CharField("Nome do Usuário",max_length=50)  # Field name made lowercase.
    loginusuario = models.CharField("Login",max_length=50, blank=True, null=True)  # Field name made lowercase.
    usuariotipo =  models.CharField("Tipo",max_length=10, blank=False, null=False,choices=USUARIO_TIPO)
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.
    lider = models.BooleanField(db_column='Lider',default=False)  # Field name made lowercase.
    descricao = models.TextField("Descrição",max_length=50, blank=True,null=True)  # Field name made lowercase.



    def __str__(self):
        return self.nomeusuario



    class Meta:
        managed = True
        db_table = 'Usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nomeusuario',]







class Equipe(models.Model):
    PERFIL_TIPO = (
        ('DEV', 'Desenvolvimento'),
        ('SUS', 'Sustentação'),
    )
    idequipe = models.AutoField(primary_key=True)  # Field name made lowercase.
    nomeequipe = models.CharField('Equipe',max_length=50,blank=False,null=False)
    equipeperfil = models.CharField("Perfil",max_length=15,choices=PERFIL_TIPO,blank=False,null=False)
    membros = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.nomeequipe



class Produto(models.Model):
    idproduto = models.AutoField(primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField('Nome do Produto', db_column='NomeProduto', max_length=50,blank=False,null=False)  # Field name made lowercase.
    novaarquitetura = models.BooleanField(db_column='NovaArquitetura')  # Field name made lowercase.
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE,blank=False,null=False)
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.


    def __str__(self):
        return self.nomeproduto

    class Meta:
        managed = True
        db_table = 'Produto'
        ordering = ["nomeproduto",]
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

class Projeto(models.Model):
    idprojeto = models.AutoField(primary_key=True)  # Field name made lowercase.
    nomeprojeto = models.CharField(db_column='NomeProjeto', max_length=50)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.
    equipe = models.ForeignKey(Equipe,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    #datainclusao = models.DateTimeField(db_column='DataInclusao')  # Field name made lowercase.
    #usuarioinclusao = models.CharField(db_column='UsuarioInclusao', max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.nomeprojeto

    class Meta:
        managed = True
        db_table = 'Projeto'





class Produtosysdatabase(models.Model):
    idprodutosysdba = models.AutoField(primary_key=True)
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='IdProduto' #, primary_key = True
                                , verbose_name='Produto')  # Field name made lowercase.
    database_name = models.CharField("Banco de Dados", db_column='Database_name', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return str(self.idproduto)

    class Meta:
        managed = True
        db_table = 'ProdutoSysDatabase'
        unique_together = (('idproduto', 'database_name'),)
        verbose_name = 'Banco vinculado a produto'
        verbose_name_plural = 'Bancos vinculados a Produtos'



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
        managed = True
        db_table = 'Permissoes'
        verbose_name = 'Lista de Permissões'
        verbose_name_plural = 'Lista de Permissões'

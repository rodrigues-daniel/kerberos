# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Grupo(models.Model):
    idgrupo = models.AutoField(db_column='IdGrupo', primary_key=True)  # Field name made lowercase.
    nomegrupo = models.CharField("Nome do Grupo",db_column='NomeGrupo', max_length=50)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.
    #datainclusao = models.DateTimeField(db_column='DataInclusao')  # Field name made lowercase.
    #usuarioinclusao = models.CharField(db_column='UsuarioInclusao', max_length=20)  # Field name made lowercase.



    def __str__(self):
        return self.nomegrupo

    class Meta:
        managed = False
        db_table = 'Grupo'
        ordering = ["nomegrupo",]
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'


class Produto(models.Model):
    idproduto = models.AutoField(db_column='IdProduto', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField('Nome do Produto', db_column='NomeProduto', max_length=50)  # Field name made lowercase.
    novaarquitetura = models.BooleanField(db_column='NovaArquitetura')  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.
    #datainclusao = models.DateTimeField(db_column='DataInclusao')  # Field name made lowercase.
    #usuarioinclusao = models.CharField(db_column='UsuarioInclusao', max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.nomeproduto

    class Meta:
        managed = False
        db_table = 'Produto'
        ordering = ["nomeproduto",]
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Produtogrupo(models.Model):
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='IdProduto', primary_key=True, verbose_name='Produto')  # Field name made lowercase.
    idgrupo = models.ForeignKey(Grupo, models.DO_NOTHING, db_column='IdGrupo', verbose_name='Grupo')  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.
    #datainclusao = models.DateTimeField(db_column='DataInclusao')  # Field name made lowercase.
    #usuarioinclusao = models.CharField(db_column='UsuarioInclusao', max_length=20)  # Field name made lowercase.


    def __str__(self):
        return " %s - %s" % (self.idproduto, self.idgrupo)



    class Meta:
        managed = False
        db_table = 'ProdutoGrupo'
        unique_together = (('idproduto', 'idgrupo'),)
        verbose_name = 'Produto - Grupo'
        verbose_name_plural = 'Produtos - Grupos'
        ordering = ['idproduto', 'idgrupo']


class Produtoprojeto(models.Model):
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='IdProduto', primary_key=True)  # Field name made lowercase.
    idprojeto = models.ForeignKey('Projeto', models.DO_NOTHING, db_column='IdProjeto')  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.
    #datainclusao = models.DateTimeField(db_column='DataInclusao')  # Field name made lowercase.
    #usuarioinclusao = models.CharField(db_column='UsuarioInclusao', max_length=20)  # Field name made lowercase.

    def __str__(self):
        return " %s - %s" % (self.idproduto, self.idprojeto)


    class Meta:
        managed = False
        db_table = 'ProdutoProjeto'
        unique_together = (('idproduto', 'idprojeto'),)
        verbose_name_plural = 'Produto - Projetos'


class Produtosysdatabase(models.Model):
    idprodutosysdba = models.AutoField(primary_key=True)
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='IdProduto'
                                #, primary_key = True
                                , verbose_name='Produto')  # Field name made lowercase.
    database_name = models.CharField("Banco de Dados", db_column='Database_name', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return str(self.idproduto)

    class Meta:
        managed = False
        db_table = 'ProdutoSysDatabase'
        unique_together = (('idproduto', 'database_name'),)
        verbose_name = 'Banco vinculado a produto'
        verbose_name_plural = 'Bancos vinculados a Produtos'


class Projeto(models.Model):
    idprojeto = models.AutoField(db_column='IdProjeto', primary_key=True)  # Field name made lowercase.
    nomeprojeto = models.CharField(db_column='NomeProjeto', max_length=50)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo')  # Field name made lowercase.
    #datainclusao = models.DateTimeField(db_column='DataInclusao')  # Field name made lowercase.
    #usuarioinclusao = models.CharField(db_column='UsuarioInclusao', max_length=20)  # Field name made lowercase.

    def __str__(self):
        return self.nomeprojeto

    class Meta:
        managed = False
        db_table = 'Projeto'


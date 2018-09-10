# Generated by Django 2.1.1 on 2018-09-10 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('idgrupo', models.AutoField(db_column='IdGrupo', primary_key=True, serialize=False)),
                ('nomegrupo', models.CharField(db_column='NomeGrupo', max_length=50, verbose_name='Nome do Grupo')),
                ('ativo', models.BooleanField(db_column='Ativo')),
            ],
            options={
                'verbose_name': 'Grupo',
                'verbose_name_plural': 'Grupos',
                'db_table': 'Grupo',
                'ordering': ['nomegrupo'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permissoeslist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambiente', models.CharField(db_column='ambiente', max_length=20)),
                ('grupo', models.CharField(db_column='Grupo', max_length=50)),
                ('usuario', models.CharField(db_column='usuario', max_length=50)),
                ('lider', models.BooleanField()),
                ('produto', models.CharField(db_column='produto', max_length=50)),
                ('dbname', models.CharField(db_column='dbname', max_length=50)),
                ('typeoflogin', models.CharField(db_column='typeoflogin', max_length=50)),
                ('typeofrole', models.CharField(db_column='typeofrole', max_length=50)),
                ('permissionlevel', models.CharField(db_column='permissionlevel', max_length=50)),
            ],
            options={
                'verbose_name': 'Lista de Permissões',
                'verbose_name_plural': 'Lista de Permissões',
                'db_table': 'Permissoes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('idproduto', models.AutoField(db_column='IdProduto', primary_key=True, serialize=False)),
                ('nomeproduto', models.CharField(db_column='NomeProduto', max_length=50, verbose_name='Nome do Produto')),
                ('novaarquitetura', models.BooleanField(db_column='NovaArquitetura')),
                ('ativo', models.BooleanField(db_column='Ativo')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'Produto',
                'ordering': ['nomeproduto'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produtosysdatabase',
            fields=[
                ('idprodutosysdba', models.AutoField(primary_key=True, serialize=False)),
                ('database_name', models.CharField(db_column='Database_name', max_length=100, verbose_name='Banco de Dados')),
            ],
            options={
                'verbose_name': 'Banco vinculado a produto',
                'verbose_name_plural': 'Bancos vinculados a Produtos',
                'db_table': 'ProdutoSysDatabase',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('idprojeto', models.AutoField(db_column='IdProjeto', primary_key=True, serialize=False)),
                ('nomeprojeto', models.CharField(db_column='NomeProjeto', max_length=50)),
                ('ativo', models.BooleanField(db_column='Ativo')),
            ],
            options={
                'db_table': 'Projeto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(db_column='IdUsuario', primary_key=True, serialize=False)),
                ('loginusuario', models.CharField(blank=True, db_column='LoginUsuario', max_length=50, null=True, verbose_name='Login')),
                ('nomeusuario', models.CharField(db_column='NomeUsuario', max_length=50, verbose_name='Nome do Usuário')),
                ('ativo', models.BooleanField(db_column='Ativo')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
                'db_table': 'Usuario',
                'ordering': ['nomeusuario'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarioproduto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lider', models.BooleanField(db_column='Lider')),
            ],
            options={
                'verbose_name': 'Usuário Produto - Vinculação',
                'verbose_name_plural': 'Usuários Produtos - Vinculações',
                'db_table': 'UsuarioProduto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produtogrupo',
            fields=[
                ('idproduto', models.ForeignKey(db_column='IdProduto', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kerberosadm.Produto', verbose_name='Produto')),
                ('ativo', models.BooleanField(db_column='Ativo')),
            ],
            options={
                'verbose_name': 'Produto - Grupo',
                'verbose_name_plural': 'Produtos - Grupos',
                'db_table': 'ProdutoGrupo',
                'ordering': ['idproduto', 'idgrupo'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Produtoprojeto',
            fields=[
                ('idproduto', models.ForeignKey(db_column='IdProduto', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kerberosadm.Produto')),
                ('ativo', models.BooleanField(db_column='Ativo')),
            ],
            options={
                'verbose_name_plural': 'Produto - Projetos',
                'db_table': 'ProdutoProjeto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuariogrupo',
            fields=[
                ('idusuario', models.ForeignKey(db_column='IdUsuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='kerberosadm.Usuario', verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Usuário Grupo - Vinculação',
                'verbose_name_plural': 'Usuários Grupos - Vinculações',
                'db_table': 'UsuarioGrupo',
                'ordering': ['idusuario', 'idgrupo'],
                'managed': False,
            },
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-20 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'ordering': ('fecha',),
            },
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('especie',),
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('genero',),
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('fecha_nacimiento', models.DateField()),
                ('ruta_foto', models.CharField(max_length=512)),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelos.Genero')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='OpcionMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=256)),
                ('ruta', models.CharField(blank=True, max_length=256, null=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group')),
                ('opcion_padre', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='modelos.OpcionMenu')),
            ],
            options={
                'ordering': ('label',),
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nuid', models.CharField(max_length=64, unique=True)),
                ('direccion', models.CharField(max_length=128)),
                ('telefono', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ('nuid',),
            },
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=128)),
                ('especie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelos.Especie')),
            ],
            options={
                'ordering': ('raza',),
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelos.Persona')),
                ('tarjeta_profesional', models.CharField(max_length=64, unique=True)),
                ('ruta_firma', models.CharField(max_length=512)),
            ],
            options={
                'ordering': ('tarjeta_profesional',),
            },
            bases=('modelos.persona',),
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelos.Persona')),
            ],
            options={
                'ordering': ('pk',),
            },
            bases=('modelos.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mascota',
            name='raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelos.Raza'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelos.Mascota'),
        ),
        migrations.AddField(
            model_name='mascota',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelos.Propietario'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modelos.Medico'),
        ),
    ]

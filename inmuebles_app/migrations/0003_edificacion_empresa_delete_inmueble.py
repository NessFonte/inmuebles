# Generated by Django 4.2.4 on 2024-06-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebles_app', '0002_alter_inmueble_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=250)),
                ('pais', models.CharField(max_length=150)),
                ('descripcion', models.TextField(max_length=500)),
                ('imagen', models.CharField(max_length=900)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('website', models.URLField(max_length=250)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Inmueble',
        ),
    ]

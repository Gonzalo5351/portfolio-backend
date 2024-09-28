# Generated by Django 5.1.1 on 2024-09-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('tecnologias', models.CharField(max_length=200)),
                ('enlace', models.URLField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adega', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adega',
            name='qtd_vinhos',
            field=models.IntegerField(default=10),
        ),
    ]

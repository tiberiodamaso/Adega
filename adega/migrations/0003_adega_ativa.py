# Generated by Django 4.0.4 on 2022-05-26 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adega', '0002_alter_adega_qtd_vinhos'),
    ]

    operations = [
        migrations.AddField(
            model_name='adega',
            name='ativa',
            field=models.BooleanField(default=True),
        ),
    ]

# Generated by Django 4.0.5 on 2022-08-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0003_alter_footballclubs_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballclubs',
            name='latitude',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='footballclubs',
            name='longitude',
            field=models.IntegerField(blank=True, max_length=200, null=True),
        ),
    ]

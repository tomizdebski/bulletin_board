# Generated by Django 3.2 on 2022-10-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulettin_board_app', '0006_alter_locations_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='country',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='latitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='longitude',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='locations',
            name='zipcode',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='province',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='locations',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

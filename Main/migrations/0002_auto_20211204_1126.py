# Generated by Django 3.2.9 on 2021-12-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facility',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]

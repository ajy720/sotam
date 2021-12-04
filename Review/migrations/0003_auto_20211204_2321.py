# Generated by Django 3.2.9 on 2021-12-04 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Review', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

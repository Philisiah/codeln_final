# Generated by Django 2.0.4 on 2018-11-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0020_auto_20181115_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

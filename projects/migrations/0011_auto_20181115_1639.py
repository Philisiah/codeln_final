# Generated by Django 2.0.4 on 2018-11-15 16:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0010_auto_20181115_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]

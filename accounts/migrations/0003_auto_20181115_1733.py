# Generated by Django 2.0.4 on 2018-11-15 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_auto_20181112_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='framework',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='frameworks', to='projects.Framework'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='languages', to='projects.Language'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('recruiter', 'Recruiter'), ('developer', 'Developer')],
                                   default='developer', max_length=30, null=True),
        ),
    ]

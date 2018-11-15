# Generated by Django 2.0.4 on 2018-11-15 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0021_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='framework',
        ),
        migrations.AddField(
            model_name='ongoingprojects',
            name='framework',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, to='projects.Framework'),
        ),
        migrations.AddField(
            model_name='ongoingprojects',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, to='projects.Language'),
        ),
    ]

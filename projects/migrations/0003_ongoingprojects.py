# Generated by Django 2.0.4 on 2018-11-12 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20181112_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='OngoingProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigner',
                                               to=settings.AUTH_USER_MODEL)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate',
                                                to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
        ),
    ]
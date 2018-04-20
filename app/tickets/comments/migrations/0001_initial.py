# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('text', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='When was the comment created', db_index=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='comments_created_by_user', verbose_name='Who created the comment', on_delete=models.CASCADE)),
                ('ticket', models.ForeignKey(to='tickets.Ticket', related_name='comments', verbose_name='Which ticket is this comment for', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'verbose_name': 'Comment',
                'ordering': ('created_at',),
            },
        ),
    ]

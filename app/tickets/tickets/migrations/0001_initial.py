# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Title of the ticket', max_length=128)),
                ('description', models.TextField(verbose_name='Description of the ticket')),
                ('created_at', models.DateTimeField(verbose_name='When was the ticket created', auto_now_add=True)),
                ('status', models.CharField(verbose_name='What is the status of the ticket', default='new', choices=[('new', 'New'), ('pro', 'In progress'), ('fin', 'Finished'), ('tes', 'Testing'), ('wfx', 'Wont fix')], max_length=3)),
                ('assigned_to', models.ManyToManyField(verbose_name='Who is responsible for the ticket', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(verbose_name='Who created the ticket', on_delete=models.CASCADE, related_name='tickets_created_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-10 09:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='transaction',
            name='description',
            field=models.CharField(default=' ', max_length=255),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

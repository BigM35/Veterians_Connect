# Generated by Django 4.0.4 on 2022-05-06 19:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_branch_alter_user_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='reciver', to=settings.AUTH_USER_MODEL),
        ),
    ]
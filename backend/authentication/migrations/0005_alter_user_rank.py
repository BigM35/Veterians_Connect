# Generated by Django 4.0.4 on 2022-05-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rank',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='self.determineRankTitle()'),
        ),
    ]
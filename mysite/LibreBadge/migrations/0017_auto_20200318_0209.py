# Generated by Django 3.0.3 on 2020-03-18 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibreBadge', '0016_auto_20200317_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badgetemplate',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

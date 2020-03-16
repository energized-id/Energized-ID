# Generated by Django 3.0.3 on 2020-03-16 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibreBadge', '0004_auto_20200212_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='BadgePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_title', models.CharField(max_length=200)),
                ('badge_content', models.TextField()),
                ('badge_published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.DeleteModel(
            name='WelcomeMessage',
        ),
    ]

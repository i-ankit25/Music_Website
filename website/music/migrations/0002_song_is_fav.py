# Generated by Django 2.1.2 on 2018-12-16 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
    ]
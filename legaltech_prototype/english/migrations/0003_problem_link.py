# Generated by Django 2.0.6 on 2018-09-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0002_auto_20180910_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='link',
            field=models.URLField(null=True),
        ),
    ]

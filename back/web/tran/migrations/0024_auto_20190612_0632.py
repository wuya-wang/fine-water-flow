# Generated by Django 2.1.2 on 2019-06-12 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tran', '0023_auto_20190612_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]

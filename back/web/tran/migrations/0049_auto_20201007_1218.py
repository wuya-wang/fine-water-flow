# Generated by Django 2.2.3 on 2020-10-07 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tran', '0048_auto_20201007_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like_article', to='tran.Article'),
        ),
    ]

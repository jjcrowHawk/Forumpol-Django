# Generated by Django 2.0 on 2018-01-08 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180106_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='website',
            field=models.CharField(default='', max_length=100),
        ),
    ]

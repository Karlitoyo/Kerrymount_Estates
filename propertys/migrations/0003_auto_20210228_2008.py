# Generated by Django 3.1.5 on 2021-02-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertys', '0002_auto_20210225_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
    ]

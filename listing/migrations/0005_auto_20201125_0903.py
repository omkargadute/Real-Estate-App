# Generated by Django 3.1.2 on 2020-11-25 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_auto_20201124_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='desc',
            field=models.TextField(max_length=2000),
        ),
    ]

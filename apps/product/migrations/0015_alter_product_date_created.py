# Generated by Django 4.0.6 on 2022-12-03 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 14, 14, 21, 317963)),
        ),
    ]
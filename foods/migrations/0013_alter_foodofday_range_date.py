# Generated by Django 4.1.1 on 2022-11-01 08:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0012_alter_foodofday_range_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodofday",
            name="range_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 2, 8, 24, 17, 170668, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date end",
            ),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-31 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("foods", "0011_alter_foodofday_range_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodofday",
            name="range_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2022, 11, 1, 12, 52, 21, 987786, tzinfo=datetime.timezone.utc
                ),
                verbose_name="date end",
            ),
        ),
    ]

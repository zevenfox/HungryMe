# Generated by Django 3.2.14 on 2022-10-30 07:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0013_auto_20221030_0648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodofday',
            name='menu_name',
        ),
        migrations.AddField(
            model_name='foodofday',
            name='menu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='foods.menu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodofday',
            name='range_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 7, 5, 57, 781274, tzinfo=utc), verbose_name='date end'),
        ),
    ]

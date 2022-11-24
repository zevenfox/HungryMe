# Generated by Django 3.2.7 on 2022-10-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='name',
            new_name='menu_name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='creator',
        ),
        migrations.AddField(
            model_name='menu',
            name='creator_name',
            field=models.CharField(default='Official HungryMe', max_length=50),
        ),
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='No description', max_length=250),
        ),
        migrations.AddField(
            model_name='menu',
            name='difficulty',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='menu',
            name='kcal',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='menu',
            name='number_of_ingredients',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='menu',
            name='picture_url',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='menu',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='menu',
            name='total_cooking_time',
            field=models.CharField(default='15 minutes', max_length=25),
        ),
    ]

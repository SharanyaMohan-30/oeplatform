# Generated by Django 3.0 on 2020-09-08 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelview', '0054_auto_20200408_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='energyframework',
            name='data_preprocessing_other',
            field=models.CharField(max_length=400, null=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='energyframework',
            name='auto_model_generator',
            field=models.BooleanField(default=False, help_text='Is an auto-Model generator available that transfers an input file into a Model?', verbose_name='Auto model generator'),
        ),
        migrations.AlterField(
            model_name='energyframework',
            name='inital_release_date',
            field=models.DateField(help_text='When [YYYY-MM-DD] was the framework initially released?', max_length=30, null=True, verbose_name='Inital Release Date'),
        ),
        migrations.AlterField(
            model_name='energyframework',
            name='last_updated',
            field=models.DateField(help_text='When was the factsheet last updated? Time format is [YYYY-MM-DD].', max_length=200, null=True, verbose_name='Last updated'),
        ),
        migrations.AlterField(
            model_name='energyframework',
            name='variable_rolling_horizon',
            field=models.BooleanField(default=False, help_text='Is it possible to Model a variable Rolling Horizon with the framework?', verbose_name='Variable rolling'),
        ),
        migrations.AlterField(
            model_name='energyframework',
            name='variable_time_step',
            field=models.BooleanField(default=False, help_text='Is it possible to Model variable time steps with the framework?', verbose_name='Variable time step'),
        ),
    ]
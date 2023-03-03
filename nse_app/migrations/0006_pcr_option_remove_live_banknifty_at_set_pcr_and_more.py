# Generated by Django 4.1.5 on 2023-02-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nse_app', '0005_live_live_banknifty_live_live_nifty_live_live_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='pcr_option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banknifty_at_set_pcr', models.BooleanField(blank=True, default=False, null=True)),
                ('banknifty_pcr_stoploss', models.FloatField(blank=True, null=True)),
                ('banknifty_live_pcr', models.FloatField(blank=True, default=0)),
                ('nifty_at_set_pcr', models.BooleanField(blank=True, default=False, null=True)),
                ('nifty_live_pcr', models.FloatField(blank=True, default=0)),
                ('nifty_pcr_stoploss', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'PcrOptions',
            },
        ),
        migrations.RemoveField(
            model_name='live',
            name='banknifty_at_set_pcr',
        ),
        migrations.RemoveField(
            model_name='live',
            name='banknifty_live_pcr',
        ),
        migrations.RemoveField(
            model_name='live',
            name='nifty_at_set_pcr',
        ),
        migrations.RemoveField(
            model_name='live',
            name='nifty_live_pcr',
        ),
        migrations.AlterModelTable(
            name='live',
            table='Live Settings',
        ),
        migrations.AlterModelTable(
            name='nse_setting',
            table='Settings',
        ),
        migrations.AlterModelTable(
            name='pcr_stock_name',
            table='PcrStockName',
        ),
        migrations.AlterModelTable(
            name='stock_detail',
            table='StocksDetails',
        ),
    ]
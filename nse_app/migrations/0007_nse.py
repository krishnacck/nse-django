# Generated by Django 4.1.3 on 2022-11-17 05:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("nse_app", "0006_nse_data_remove_nse_model_stop_loss_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="nse",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("strike_price", models.FloatField()),
                ("bid_price", models.FloatField()),
                ("buy_time", models.DateTimeField(auto_now=True)),
                ("live_price", models.FloatField()),
                ("pcr_value", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
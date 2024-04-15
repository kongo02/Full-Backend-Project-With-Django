# Generated by Django 5.0.4 on 2024-04-15 18:44

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="about_me",
            field=models.TextField(
                default="Say Something About Yourself", verbose_name="About Me"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="+27721046440",
                max_length=30,
                region=None,
                verbose_name="Phone Number",
            ),
        ),
    ]

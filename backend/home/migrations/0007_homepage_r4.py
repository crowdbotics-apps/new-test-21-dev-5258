# Generated by Django 2.2.12 on 2020-07-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="r4",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

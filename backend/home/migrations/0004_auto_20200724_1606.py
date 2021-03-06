# Generated by Django 2.2.12 on 2020-07-24 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0003_r123_r456_r789"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="r1",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="r2",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="homepage_r2",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

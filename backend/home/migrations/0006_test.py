# Generated by Django 2.2.12 on 2020-07-24 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_homepage_r3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_schedule', to='home.R789')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

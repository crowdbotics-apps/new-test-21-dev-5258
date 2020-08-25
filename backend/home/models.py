from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    title = models.CharField(max_length=150,)
    r1 = models.BigIntegerField(null=True, blank=True,)

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    r2 = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_r2",
    )
    r3 = models.ForeignKey(
        "home.R456",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="homepage_r3",
    )
    r4 = models.BooleanField(null=True, blank=True,)

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class R789(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class R123(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()


class R456(models.Model):
    "Generated Model"
    r2 = models.BigIntegerField()


class Test(models.Model):
    "Generated Model"
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="test_user",
    )
    schedule = models.ForeignKey(
        "home.R789", on_delete=models.CASCADE, related_name="test_schedule",
    )


class NEW1(models.Model):
    "Generated Model"
    r1 = models.BigIntegerField()

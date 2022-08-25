from django.db import models


class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    sales = models.JSONField()

    def __str__(self):
        return self.location

    @property
    def total(self):
        return sum(self.sales)

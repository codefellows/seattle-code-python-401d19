from django.contrib.auth import get_user_model
from django.db import models


class Snack(models.Model):
    name = models.CharField(max_length=256)
    purchaser = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

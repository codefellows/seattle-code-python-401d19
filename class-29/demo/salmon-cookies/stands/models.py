from django.db import models

class Stand(models.Model):
    location = models.CharField(max_length=64)
    sales = models.JSONField()  # 7am - 7pm sales figures

    def __str__(self):
        return self.location

    @property
    def total(self):
        return sum(self.sales)

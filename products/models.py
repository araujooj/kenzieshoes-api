from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.title

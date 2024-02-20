from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name

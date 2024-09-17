import uuid
from django.db import models

class ProductDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    stock = models.IntegerField()

    @property
    def is_in_stock(self):
        return self.stock > 0

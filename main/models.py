import uuid
from django.db import models
from django.contrib.auth.models import User

class ProductDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=255)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/', default='default_image.png')


    @property
    def is_in_stock(self):
        return self.stock > 0
    
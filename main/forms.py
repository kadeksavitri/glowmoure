from django.forms import ModelForm
from main.models import ProductDetail

class ProductDetailForm(ModelForm):
    class Meta:
        model = ProductDetail
        fields = ["name", "price", "description", "category", "stock", 'image']








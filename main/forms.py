from django.forms import ModelForm
from main.models import ProductDetail
from django.utils.html import strip_tags

class ProductDetailForm(ModelForm):
    class Meta:
        model = ProductDetail
        fields = ["name", "price", "description", "category", "stock", 'image']

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)








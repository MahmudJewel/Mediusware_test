from django import forms
from product import models

class productForm(forms.ModelForm):
    class Meta(object):
        model = models.Product
        fields = '__all__'
        
class ProductImageForm(forms.ModelForm):
    class Meta(object):
        model = models.ProductImage
        fields = ['file_path']
        
class ProductVariantPriceForm(forms.ModelForm):
    class Meta(object):
        model = models.ProductVariantPrice
        fields = ['product_variant_one','product_variant_two','product_variant_three','price','stock']
        

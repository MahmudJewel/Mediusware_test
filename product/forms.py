from django import forms
from product import models

class productForm(forms.ModelForm):
    class Meta(object):
        model = models.Product
        fields = '__all__'
        
class ProductImageForm(forms.ModelForm):
    class Meta(object):
        model = models.ProductImage
        fields = '__all__'
        
class ProductImageForm(forms.ModelForm):
    class Meta(object):
        model = models.ProductImage
        fields = ['file_path']
        

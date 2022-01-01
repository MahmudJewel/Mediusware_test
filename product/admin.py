from django.contrib import admin
from product import models
# Register your models here.
admin.site.register(models.Variant)
admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.ProductVariant)
admin.site.register(models.ProductVariantPrice)


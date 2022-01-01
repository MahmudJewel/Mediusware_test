from django.shortcuts import render
from product import models

# Create your views here.
def home_view(request):
    pd = models.Product.objects.get(id=1)
    pvprice= models.ProductVariantPrice.objects.filter(product=pd)
    print(f"price: {pvprice}")
    vrprice=models.Product.objects.get(id=1).productvariantprice_set.all()
    variant=models.Product.objects.get(id=1).productvariant_set.all()
    stock=models.Product.objects.get(id=1).productvariant_set.all()
    print(f"variantprice: {vrprice} \n variant: {variant}\nstock: ")
    Products=models.Product.objects.all()
    # print(f"Products are: {Products.productvariantprice_set.all()}")
    context={
        'Products':Products,
    }
    return render(request, 'home.html',context)

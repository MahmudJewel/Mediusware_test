from django.shortcuts import render
from product import models
# for paginations 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home_view(request):
    # pd = models.Product.objects.get(id=1)
    # pvprice= models.ProductVariantPrice.objects.filter(product=pd)
    # print(f"price: {pvprice}")
    # vrprice=models.Product.objects.get(id=1).productvariantprice_set.all()
    # variant=models.Product.objects.get(id=1).productvariant_set.all()
    # stock=models.Product.objects.get(id=1).productvariant_set.all()
    # print(f"variantprice: {vrprice} \n variant: {variant}\nstock: ")
    products=models.Product.objects.all()
    product_num = products.count()
    
    # for paginations 
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 2)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context={
        'products':products,
        'product_num':product_num,
    }
    return render(request, 'home.html',context)

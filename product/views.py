from django.shortcuts import render
from product import models
# for paginations 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from product import forms

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
    
    # for dropdown variant 
    variant = models.Variant.objects.all()
    
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
        'variant':variant
    }
    return render(request, 'home.html',context)

# search bar 
def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('inputTitle') # get the title from search
        dropdown = request.GET.get('dropdown') # get the choice from search
        priceFrom = request.GET.get('from') # get the price from search
        priceTo = request.GET.get('to')
        # converting string to int & for empty logic applied 
        if (priceFrom !=''):
            priceFrom = int(priceFrom)
        else:
            priceFrom = 0
        if (priceTo !=''):
            priceTo = int(priceTo)
        else:
            priceTo = 9999999
            
        # print(f"search : {type(priceFrom)}")
        # searchItem = models.Product.objects.filter(title__contains = search)
        # searchItem = models.Product.objects.filter(productvariant__variant__title = dropdown)
        
        # chaining filter 
        searchItem = models.Product.objects.filter(productvariantprice__price__gte = priceFrom, productvariantprice__price__lte = priceTo).filter(title__contains = search).filter(productvariant__variant__title = dropdown)
        context = {
            'products':searchItem,
        }
    return render(request, 'search.html', context)

# add product page 
def add_product_view(request):
    productForm = forms.productForm
    ProductImageForm = forms.ProductImageForm
    ProductVariantPriceForm = forms.ProductVariantPriceForm
    context={
        'productForm':productForm,
        'ProductImageForm' : ProductImageForm,
        'ProductVariantPriceForm':ProductVariantPriceForm,
    }
    return render(request, 'productAdd.html', context)

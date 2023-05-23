from django.shortcuts import render, redirect

import store_app.models as sam



# from store_app import Product


def BASE(request):
    return render(request, 'Main/base.html')




def HOME(request):
    product = sam.Product.objects.filter(status='Publish')

    context = {
        'product': product,
    }
    return render(request, 'Main/index.html', context)


def PRODUCT(request):
    product = sam.Product.objects.filter(status='Publish')
    categories = sam.Categories.objects.all()
    filter_price = sam.Filter_Price.objects.all()
    color = sam.Color.objects.all()
    brand = sam.Brand.objects.all()

    CATID = request.GET.get('categories')
    if CATID:
        product = sam.Product.objects.filter(categories = CATID)
    else:
        product = sam.Product.objects.filter(status='Publish')

    context = {
        'product': product,
        'categories': categories,
        'filter_price': filter_price,
        'color': color,
        'brand': brand,

    }

    return render(request, 'Main/product.html', context)


def SEARCH(request):
    query = request.GET.get('query')
    product = sam.Product.objects.filter(name__icontains = query)
    context = {
        'product': product,

    }
    return render(request, 'Main/search.html', context)


def Contact_Page(request):
    return render(request, 'Main/contact.html')
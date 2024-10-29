from django.template.context_processors import request

from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'practice/product_list.html', {'products': products})

def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'practice/product_details.html', {'product': product})
from django.shortcuts import render
from .models import Products

# Create your views here.
def index(request):
    products_objects = Products.objects.all()
    return render(request,'index.html',{'products_objects':products_objects})

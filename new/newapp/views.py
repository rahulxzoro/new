from django.shortcuts import render
from . models import Category,Product
# Create your views here.
def home(request):
    obj=Product.objects.all().filter(available=True)

    return render(request,'category.html',{"obj":obj})


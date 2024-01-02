from django.shortcuts import render,get_object_or_404
from . models import Category,Product
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page,available=True)
    else:    
        product_list=Product.objects.all().filter(available=True)

    return render(request,'category.html',{"product":product_list,'category':c_page})

def detail(request,id):
    details=Product.objects.get(id=id)
    
    return render(request,'detail.html',{'prod':details})


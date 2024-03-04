from django.shortcuts import render,get_object_or_404
from . models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def home(request,c_slug=None):
    c_page=None
    if c_slug!=None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page,available=True)
    else:    
        product_list=Product.objects.all().filter(available=True)

    paginator = Paginator(product_list,8) 
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    try:
        
        products = paginator.page(page)
    except(EmptyPage,InvalidPage):
        products =paginator.page(paginator.num_pages)
    return render(request,'category.html',{"product":products,'category':c_page})

def detail(request,id,c_slug=None):
    details=Product.objects.get(id=id)
    
    return render(request,'detail.html',{'prod':details})


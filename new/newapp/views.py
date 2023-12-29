from django.shortcuts import render
from . models import Category,Product
# Create your views here.
def home(request):
    obj=Category.objects.all()

    return render(request,'index.html',{"result":obj})

def details(request,id):
    data=Product.objects.get(id=id)
    
    return render(request,'details.html',{"data":data})

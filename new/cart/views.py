from django.shortcuts import render, redirect
from newapp.models import Product
from .models import Cartpage
from django.contrib import messages

# Create your views here.
def cart(request, id):
    product = Product.objects.get(id=id)
    user_id=None
    try:
        user_id = request.session['user']
    except:
        return redirect('credential:login')
    try:
        cartitem = Cartpage.objects.get(product=product)
        if cartitem.quantity < cartitem.product.stock:
            cartitem.quantity += 1
            cartitem.save()
    except Cartpage.DoesNotExist: 
        cartitem = Cartpage(product=product, user_id=user_id, quantity=1)
        cartitem.save()

    
    return redirect('cart:display')

def display(request):
    user_id = request.session.get('user', None)
   
    data = Cartpage.objects.all().filter(user_id=user_id)
    
    total_amount = sum(item.product.price * item.quantity for item in data)

        
    return render(request, 'cart.html', {'cart': data,"total_amount": total_amount})
def delete(request,id):
    user_id = request.session['user']
    product=Product.objects.get(id=id)
    categoty=Cartpage.objects.get(product=product,user_id=user_id)
    categoty.delete()
   
    return redirect('cart:display')
    
def dele(request,id):
    
    user_id = request.session['user']
    product=Product.objects.get(id=id)
    cartitem = Cartpage.objects.get(product=product,user_id=user_id)
    if cartitem.quantity >1:
            cartitem.quantity -= 1
            cartitem.save()
    return redirect('cart:display')

def buy(req):
    cart_items = Cartpage.objects.all()

    for cart_item in cart_items:
        product = cart_item.product
        quantity_to_purchase = cart_item.quantity

        if product.stock >= quantity_to_purchase:
            product.stock -= quantity_to_purchase
            product.save()
            Cartpage.objects.all().delete()
        else:
            cart_item.delete()
            
            # Show an alert box indicating insufficient stock
            messages.warning(req,f"Insufficient stock for {product.name}. Item removed from the cart.")

            return redirect('cart:display')
    return redirect('/')
    


    
    
    
    


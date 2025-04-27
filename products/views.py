from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django import forms
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, slug):
    product = Product.objects.filter(slug=slug).first()
    if not product:
        return redirect('products:product_list')
    return render(request, 'products/product_detail.html', {'product': product})

class ContactForm(forms.Form):
    name = forms.CharField(label='Ism', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Xabar', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Bu yerda email yuborish yoki ma'lumotlarni saqlash mumkin
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            form = ContactForm()  # Formani tozalash
    else:
        form = ContactForm()
    return render(request, 'products/contact.html', {'form': form})

def add_to_cart(request, slug):
    cart = request.session.get('cart', [])
    if slug not in cart:
        cart.append(slug)
        request.session['cart'] = cart
    return redirect('products:cart')

def remove_from_cart(request, slug):
    cart = request.session.get('cart', [])
    if slug in cart:
        cart.remove(slug)
        request.session['cart'] = cart
    return redirect('products:cart')

def cart_view(request):
    cart = request.session.get('cart', [])
    products = list(Product.objects.filter(slug__in=cart))
    valid_slugs = [p.slug for p in products]
    if set(cart) != set(valid_slugs):
        request.session['cart'] = valid_slugs
    return render(request, 'products/cart.html', {'products': products})

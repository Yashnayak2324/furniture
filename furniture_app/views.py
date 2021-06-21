from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request,'base.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def products(request):
    return render(request,'products.html')

def register(request):
    return render(request,'register.html')

def single(request):
    return render(request,'single.html')




